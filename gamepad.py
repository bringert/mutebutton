import hotplug

import hid
import logging
from logging import debug
import threading
import time

# TODO: This should be read from the HID report descriptor
NUM_BUTTONS = 16

class GamepadManager:
  def __init__(self, button_handler, gamepad_added=None, gamepad_removed=None):
    self.button_handler = button_handler
    self.gamepad_added = gamepad_added
    self.gamepad_removed = gamepad_removed
    self.devices = {}
    self.devmgr = hotplug.HotplugDeviceManager(self.added_callback, self.removed_callback)
    self.devmgr.start()

  def close(self):
    self.devmgr.close()

  def is_gamepad(self, vendor_id, product_id):
    # hid.enumerate() returns multiple entries for a single device
    for device in hid.enumerate(vendor_id=vendor_id, product_id=product_id):
      usage_page = device['usage_page']
      usage = device['usage']
      if usage_page == 0x01 and (usage == 0x04 or usage == 0x05):
        return True
    return False

  def make_gamepad(self, device):
    vendor_id = device.getVendorID()
    product_id = device.getProductID()

    if self.is_gamepad(vendor_id, product_id):
      # TODO: catch any exceptions and return None
      gamepad = Gamepad(vendor_id, product_id, self.button_handler)
      gamepad.start()
      return gamepad

    return None

  def added_callback(self, device):
    gamepad = self.make_gamepad(device)
    if gamepad:
      self.devices[device] = gamepad
      if self.gamepad_added:
        self.gamepad_added(gamepad)

  def removed_callback(self, device):
    gamepad = self.devices.pop(device, None)
    if gamepad:
      if self.gamepad_removed:
        self.gamepad_removed(gamepad)
      gamepad.close()


class Gamepad:
  def __init__(self, vendor_id, product_id, button_pressed):
    self.vendor_id = vendor_id
    self.product_id = product_id
    self.button_pressed = button_pressed
    self.button_state = [False] * NUM_BUTTONS
    self.running = False
    self.thread = None

  def start(self):
    self.device = hid.device()
    self.device.open(self.vendor_id, self.product_id)
    self.device.set_nonblocking(False)
    self.running = True
    thread_name = f"{self.vendor_id:04x}:{self.product_id:04x}"
    self.thread = threading.Thread(target=self.run, name=thread_name, daemon=False)
    self.thread.start()

  def close(self):
    debug("Gamepad.close()")
    self.running = False
    if self.thread:
      self.thread.join()
      self.thread = None

  def get_button_state(self, buttons_bitmap, button_index):
    byte_index = button_index // 8
    bit_index = button_index % 8
    return bool((buttons_bitmap[byte_index] >> bit_index) & 0x1)

  def handle_report(self, report):
    debug("Report: %s", report)

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
    debug("Thread started")
    try:
      while self.running:
        report = self.device.read(64, timeout_ms=1000)
        if report:
          self.handle_report(report)
    except OSError:
      debug("Caught OSError")
    self.device.close()
    debug("Thread finished")

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s")

  def button_handler(button):
    debug("button_handler(%d)", button)

  mgr = GamepadManager(button_handler)
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    pass
  print("Exiting...")
  mgr.close()
