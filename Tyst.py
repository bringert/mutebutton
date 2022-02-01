import actions
import gamepad

import logging
from logging import debug
import rumps

BUTTON_MUTE = 1

class MuteButtonApp(rumps.App):
  def __init__(self):
    super(MuteButtonApp, self).__init__("Tyst")
    self.icon = "icon.icns"
    self.quit_button = None
    self.menu = ["Teams: Mute", "Quit"]
    self.gamepad_mgr = gamepad.GamepadManager(self.button_handler)

  @rumps.clicked('Quit')
  def clean_up_before_quit(self, _):
    debug("Quitting")
    self.gamepad_mgr.close()
    rumps.quit_application()

  @rumps.clicked('Teams: Mute')
  def teams_mute(self, _):
    actions.ms_teams_mute()

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      debug(f"Button {button} pressed")
      actions.ms_teams_mute()

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s")
  app = MuteButtonApp()
  app.run()
