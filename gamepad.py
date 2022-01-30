import hid

DEBUG = True

# TODO: This should be read from the HID report descriptor
NUM_BUTTONS = 16

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
    self.button_state = [False] * NUM_BUTTONS

  def close():
    self.gamepad.close()

  def get_button_state(self, buttons_bitmap, button_index):
    byte_index = button_index // 8
    bit_index = button_index % 8
    return bool((buttons_bitmap[byte_index] >> bit_index) & 0x1)

  def check_buttons(self):
#    if DEBUG:
#      print(f"Reading from device 0x{self.vendor_id:04x}:0x{self.product_id:04x}...")
    report = self.gamepad.read(64)
    if DEBUG:
      print(f"From device 0x{self.vendor_id:04x}:0x{self.product_id:04x}: {report}")
    if report:
      # The first byte is the report ID
      # After that, the button values are packed into bytes
      # TODO: need to ignore non-button reports
      buttons_bitmap = report[1:(1 + NUM_BUTTONS//8)]
      for button in range(0, NUM_BUTTONS):
        new_value = self.get_button_state(buttons_bitmap, button)
        if new_value != self.button_state[button]:
          self.button_state[button] = new_value
          if new_value:
            self.button_pressed(button)
