# Dependencies:
# brew install libusb1
# pip3 install -U libusb1 --user

import logging
from logging import debug, error
import usb1
import threading
import time

class HotplugDeviceManager:
  def __init__(self, added_callback=None, removed_callback=None):
    self.added_callback = added_callback
    self.removed_callback = removed_callback
    self.device_handles = {}
    self.pending_callbacks = []
    self.running = False
    self.thread = None

  def start(self):
    self.running = True
    self.thread = threading.Thread(target=self.run, name="HotplugDeviceManager", daemon=False)
    self.thread.start()

  def close(self):
    debug("Closing HotplugDeviceManager")
    self.running = False
    if self.thread:
      self.thread.join()
      self.thread = None

  def hotplug_callback(self, context, device, event):
    if event == usb1.HOTPLUG_EVENT_DEVICE_ARRIVED:
      self.handle_added(device)
    elif event == usb1.HOTPLUG_EVENT_DEVICE_LEFT:
      self.handle_removed(device)
    return False # Stay registered

  def handle_added(self, device):
    debug("Added %s", device)
    handle = HotplugDeviceHandle(device)
    self.device_handles[device] = handle
    if self.added_callback:
      self.added_callback(handle)

  def handle_removed(self, device):
    debug("Removed %s", device)
    handle = self.device_handles[device]
    del self.device_handles[device]
    if self.removed_callback:
      self.removed_callback(handle)

  def remove_devices(self):
    debug("Removing all devices")
    # Use list() since we remove the values from the dict in handle_removed()
    for device in list(self.device_handles.keys()):
      self.handle_removed(device)

  def run(self):
    with usb1.USBContext() as context:
      if not context.hasCapability(usb1.CAP_HAS_HOTPLUG):
        error('Hotplug support is missing. Please update your libusb version.')
        return
      debug("Registering hotplug callback...")
      opaque = context.hotplugRegisterCallback(self.hotplug_callback,
          # Which events to handle
          events=usb1.HOTPLUG_EVENT_DEVICE_ARRIVED | usb1.HOTPLUG_EVENT_DEVICE_LEFT,
          # List all matching devices when registering the callback
          flags=usb1.HOTPLUG_ENUMERATE,
          vendor_id=usb1.HOTPLUG_MATCH_ANY,
          product_id=usb1.HOTPLUG_MATCH_ANY,
          dev_class=usb1.HOTPLUG_MATCH_ANY)
      debug("Callback registered. Monitoring events")
      while self.running:
        context.handleEventsTimeout(tv=1)
      self.remove_devices()
    debug("HotplugDeviceManager thread exiting")

class HotplugDeviceHandle(object):
  def __init__(self, device):
    self.device = device
    self.user_object = None

  @property
  def vendor_id(self):
    return self.device.getVendorID()

  @property
  def product_id(self):
    return self.device.getProductID()


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s")

  def arrived_callback(handle):
    print(f"added {handle.vendor_id:04x}:{handle.product_id:04x}")
  def left_callback(handle):
    print(f"removed {handle.vendor_id:04x}:{handle.product_id:04x}")

  devmgr = HotplugDeviceManager(arrived_callback, left_callback)
  try:
    devmgr.start()
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting")
    devmgr.close()
