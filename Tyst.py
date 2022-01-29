import hid
import os
import rumps
import threading
import time

BUTTON_MUTE = 1

# U+1F92B Shushing face / Face with Finger Covering Closed Lips
STATUS_BAR_EMOJI = "\U0001F92B"

class MuteButtonApp(object):
  def __init__(self):
    self.app = rumps.App("Mute test", STATUS_BAR_EMOJI)

  def find_joysticks_and_gamepads(self):
    joysticks = []
    for device in hid.enumerate():
      usage_page = device['usage_page']
      usage = device['usage']
      if usage_page == 0x01 and (usage == 0x04 or usage == 0x05):
        joysticks.append(device)
    return joysticks

  def watch_mute_buttons(self):
    for joystick in self.find_joysticks_and_gamepads():
      thread = threading.Thread(target=self.watch_mute_button, args=(joystick,), daemon=True)
      thread.start()

  def watch_mute_button(self, joystick):
    device = JoystickButton(joystick, self.button_handler)
    while True:
      device.check_buttons()

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      self.ms_teams_mute()

  def ms_teams_mute(self):
    print("Toggling mute in Microsoft Teams...")
    os.system('osascript microsoft-teams-mute.applescript')

  def run(self):
    self.watch_mute_buttons()
    self.app.run()

class JoystickButton:
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

if __name__ == '__main__':
  app = MuteButtonApp()
  app.run()
