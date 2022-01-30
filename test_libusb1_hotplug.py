# Dependencies:
# brew install libusb1
# pip3 install -U libusb1 --user

import usb1

class USBDeviceManager:
  # If arrived_callback returns None,
  def __init__(self, arrived_callback, left_callback=None):
    self.arrived_callback = arrived_callback
    self.left_callback = left_callback

  def hotplug_callback(self, context, device, event):
    vendor_id = device.getVendorID()
    product_id = device.getProductID()

    if event == usb1.HOTPLUG_EVENT_DEVICE_ARRIVED:
      open_dev = self.arrived_callback(vendor_id, product_id)
    elif event == usb1.HOTPLUG_EVENT_DEVICE_LEFT:
      if self.left_callback:
        self.left_callback(vendor_id, product_id)

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
      print('Callback registered. Monitoring events, ^C to exit')
      try:
        while True:
          context.handleEvents()
      except (KeyboardInterrupt, SystemExit):
        print('Exiting')

if __name__ == '__main__':
  def arrived_callback(vendor_id, product_id):
    print(f"Device arrived: 0x{vendor_id:04x}:0x{product_id:04x}")
  def left_callback(vendor_id, product_id):
    print(f"Device left: 0x{vendor_id:04x}:0x{product_id:04x}")
  USBDeviceManager(arrived_callback, left_callback).run()


# Output on start:
# Device arrived: Bus 020 Device 003: ID 2341:8037

# Output when unplugging Arduino Micro
# Device left: Bus 020 Device 003: ID 2341:8037
# Device arrived: Bus 020 Device 013: ID 2341:8037
