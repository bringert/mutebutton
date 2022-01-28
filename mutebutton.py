import hid
import os
import time

VENDOR_ID = 0x2341
PRODUCT_ID = 0x8037

BUTTON_MUTE = 1

class JoystickButton:
  def __init__(self, vendor_id, product_id, button_pressed):
    self.gamepad = hid.device()
    self.gamepad.open(vendor_id, product_id)
    self.gamepad.set_nonblocking(True)
    self.button_pressed = button_pressed

  def check_buttons(self):
    report = self.gamepad.read(64)
    if report:
      #print(report)
      button1 = (report[1] & 0x02) >> 1
      print("Button 1:", button1)
      if button1:
        self.button_pressed(1)

class MuteButton:
  def __init__(self):
    self.input = JoystickButton(VENDOR_ID, PRODUCT_ID, self.button_handler)

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      self.ms_teams_mute()

  def ms_teams_mute(self):
    print("Toggling mute in Microsoft Teams...")
    os.system('osascript microsoft-teams-mute.applescript')

  def check_buttons(self):
    self.input.check_buttons()

def main():
  mute = MuteButton()
  while True:
    mute.check_buttons()
    time.sleep(0.01)

if __name__ == '__main__':
  main()
