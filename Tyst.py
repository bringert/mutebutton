import hid
import os
import rumps
import threading
import time

VENDOR_ID = 0x2341
PRODUCT_ID = 0x8037

BUTTON_MUTE = 1

# U+1F92B Shushing face / Face with Finger Covering Closed Lips
STATUS_BAR_EMOJI = "\U0001F92B"

class MuteButtonApp(object):
  def __init__(self):
    self.app = rumps.App("Mute test", STATUS_BAR_EMOJI)

  def watch_mute_button(self):
    device = JoystickButton(VENDOR_ID, PRODUCT_ID, self.button_handler)
    while True:
      device.check_buttons()
      time.sleep(0.01)

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      self.ms_teams_mute()

  def ms_teams_mute(self):
    print("Toggling mute in Microsoft Teams...")
    os.system('osascript microsoft-teams-mute.applescript')

  def run(self):
    thread = threading.Thread(target=self.watch_mute_button, daemon=True)
    thread.start()
    self.app.run()

class JoystickButton:
  def __init__(self, vendor_id, product_id, button_pressed):
    self.gamepad = hid.device()
    self.gamepad.open(vendor_id, product_id)
    self.gamepad.set_nonblocking(False)
    self.button_pressed = button_pressed

  def check_buttons(self):
    print("Reading from device...")
    report = self.gamepad.read(64)
    if report:
      button1 = (report[1] & 0x02) >> 1
      print("Button 1:", button1)
      if button1:
        self.button_pressed(1)

if __name__ == '__main__':
  app = MuteButtonApp()
  app.run()
