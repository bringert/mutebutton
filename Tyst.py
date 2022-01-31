import actions
import gamepad

import logging
from logging import debug
import rumps

BUTTON_MUTE = 1

class MuteButtonApp(object):
  def __init__(self):
    self.gamepad_mgr = gamepad.GamepadManager(self.button_handler)
    self.app = rumps.App("Mute test", icon="icon.icns",
        menu=['Quit'], quit_button=None)

  @rumps.clicked('Quit')
  def clean_up_before_quit(_):
    debug("Quitting")
    # TODO: For some reason this hangs and never happens
    #self.gamepad_mgr.close()
    rumps.quit_application()

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      print(f"Button {button} pressed")
      actions.ms_teams_mute()

  def run(self):
    self.app.run()

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s")
  app = MuteButtonApp()
  app.run()
