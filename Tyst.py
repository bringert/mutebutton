import actions
import gamepad

import rumps

BUTTON_MUTE = 1

class MuteButtonApp(object):
  def __init__(self):
    self.app = rumps.App("Mute test", icon="icon.icns")

  def watch_mute_buttons(self):
    for device in gamepad.find_joysticks_and_gamepads():
      gamepad.Gamepad(device, self.button_handler).start()

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      print(f"Button {button} pressed")
      actions.ms_teams_mute()

  def run(self):
    self.watch_mute_buttons()
    self.app.run()

if __name__ == '__main__':
  app = MuteButtonApp()
  app.run()
