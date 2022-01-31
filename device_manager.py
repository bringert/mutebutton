# Dependencies:
# brew install libusb1
# pip3 install -U libusb1 --user

import usb1
import threading
import time

class HotplugDeviceManager:
  # If arrived_callback returns None,
  def __init__(self, added_callback=None, removed_callback=None):
    self.added_callback = added_callback
    self.removed_callback = removed_callback
    self.devices = {}
    self.pending_callbacks = []
    self.running = False

  def start(self):
    self.running = True
    self.thread = threading.Thread(target=self.run, daemon=False)
    self.thread.start()

  def close(self):
    self.running = False
    self.thread.join()

  def hotplug_callback(self, context, device, event):
    vendor_id = device.getVendorID()
    product_id = device.getProductID()

    if event == usb1.HOTPLUG_EVENT_DEVICE_ARRIVED:
      handle = HotplugDeviceHandle(device)
      self.devices[device] = handle
      if self.added_callback:
        self.added_callback(handle)
    elif event == usb1.HOTPLUG_EVENT_DEVICE_LEFT:
      handle = self.devices[device]
      del self.devices[device]
      if self.removed_callback:
        self.removed_callback(handle)

    return False # Stay registered

  def run(self):
    with usb1.USBContext() as context:
      if not context.hasCapability(usb1.CAP_HAS_HOTPLUG):
        print('Hotplug support is missing. Please update your libusb version.')
        return
      print('Registering hotplug callback...')
      opaque = context.hotplugRegisterCallback(self.hotplug_callback,
          # Which events to handle
          events=usb1.HOTPLUG_EVENT_DEVICE_ARRIVED | usb1.HOTPLUG_EVENT_DEVICE_LEFT,
          # List all matching devices when registering the callback
          flags=usb1.HOTPLUG_ENUMERATE,
          vendor_id=usb1.HOTPLUG_MATCH_ANY,
          product_id=usb1.HOTPLUG_MATCH_ANY,
          dev_class=usb1.HOTPLUG_MATCH_ANY)
      print('Callback registered. Monitoring events')
      while self.running:
        context.handleEventsTimeout(tv=1)
      print("HotplugDeviceManager thread exiting")

class HotplugDeviceHandle(object):
  def __init__(self, device):
    self.device = device

  @property
  def vendor_id(self):
    return self.device.getVendorID()

  @property
  def product_id(self):
    return self.device.getProductID()


if __name__ == '__main__':
  def arrived_callback(handle):
    print(f"Device arrived: 0x{handle.vendor_id:04x}:0x{handle.product_id:04x}")
  def left_callback(handle):
    print(f"Device left: 0x{handle.vendor_id:04x}:0x{handle.product_id:04x}")

  devmgr = HotplugDeviceManager(arrived_callback, left_callback)
  try:
    devmgr.start()
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting")
    devmgr.close()


# Output on start:
# Device arrived: Bus 020 Device 003: ID 2341:8037

# Output when unplugging Arduino Micro
# Device left: Bus 020 Device 003: ID 2341:8037
# Device arrived: Bus 020 Device 013: ID 2341:8037
