import hid

def find_joysticks_and_gamepads():
  devices = []
  for device in hid.enumerate():
    usage_page = device['usage_page']
    usage = device['usage']
    if usage_page == 0x01 and (usage == 0x04 or usage == 0x05):
      devices.append(device)
  return devices

def watch_mute_button(joystick, button_handler):
  device = Gamepad(joystick, button_handler)
  while True:
    device.check_buttons()

class Gamepad:
  def __init__(self, device_dict, button_pressed):
    self.vendor_id = device_dict['vendor_id']
    self.product_id = device_dict['product_id']
    self.gamepad = hid.device()
    self.gamepad.open(self.vendor_id, self.product_id)
    self.gamepad.set_nonblocking(False)
    self.button_pressed = button_pressed

  def check_buttons(self):
    print(f"Reading from device 0x{self.vendor_id:04x}:0x{self.product_id:04x}...")
    report = self.gamepad.read(64)
    #print(report)
    if report:
      # TODO: read all the buttons
      button1 = (report[1] & 0x02) >> 1
      if button1:
        print(f"Device 0x{self.vendor_id:04x}:0x{self.product_id:04x}: button 1 pressed")
        self.button_pressed(1)
