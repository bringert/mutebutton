import logging
from logging import debug, error
import usb1
import threading
import time

class HotplugDeviceManager:
  def __init__(self, added_callback=None, removed_callback=None):
    self.added_callback = added_callback
    self.removed_callback = removed_callback
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
      if self.added_callback:
        self.added_callback(device)
    elif event == usb1.HOTPLUG_EVENT_DEVICE_LEFT:
      if self.removed_callback:
        self.removed_callback(device)
    return False # Stay registered

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
    debug("HotplugDeviceManager thread exiting")


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s")

  def arrived_callback(handle):
    print(f"added {handle.getVendorID():04x}:{handle.getProductID():04x}")
  def left_callback(handle):
    print(f"removed {handle.getVendorID():04x}:{handle.getProductID():04x}")

  devmgr = HotplugDeviceManager(arrived_callback, left_callback)
  try:
    devmgr.start()
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting")
    devmgr.close()
