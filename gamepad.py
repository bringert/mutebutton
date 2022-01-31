import hid
import threading
import time

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

class Gamepad:
  def __init__(self, device_dict, button_pressed):
    self.vendor_id = device_dict['vendor_id']
    self.product_id = device_dict['product_id']
    self.button_pressed = button_pressed
    self.button_state = [False] * NUM_BUTTONS
    self.running = False

  def start(self):
    self.gamepad = hid.device()
    self.gamepad.open(self.vendor_id, self.product_id)
    self.gamepad.set_nonblocking(False)
    self.running = True
    self.thread = threading.Thread(target=self.run, daemon=False)
    self.thread.start()

  # TODO: not yet used
  def close(self):
    self.running = False
    if self.thread:
      self.thread.join()
      self.thread = None

  def get_button_state(self, buttons_bitmap, button_index):
    byte_index = button_index // 8
    bit_index = button_index % 8
    return bool((buttons_bitmap[byte_index] >> bit_index) & 0x1)

  def handle_report(self, report):
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

  def run(self):
    while self.running:
      # if DEBUG:
      #   print(f"Reading from device 0x{self.vendor_id:04x}:0x{self.product_id:04x}...")
      report = self.gamepad.read(64, timeout_ms=1000)
      if report:
        if DEBUG:
          print(f"From device 0x{self.vendor_id:04x}:0x{self.product_id:04x}: {report}")
        self.handle_report(report)
    self.gamepad.close()



if __name__ == '__main__':
  gamepads = []
  for device in find_joysticks_and_gamepads():
    gamepad = Gamepad(device, lambda button: print(f"Button {button} pressed"))
    gamepad.start()
    gamepads.append(gamepad)
  try:
    time.sleep(4)
  except KeyboardInterrupt:
    pass
  print("Exiting...")
  for gamepad in gamepads:
    print(f"Closing 0x{gamepad.vendor_id:04x}:0x{gamepad.product_id:04x}...")
    gamepad.close()
