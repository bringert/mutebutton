import accessibility
import actions_fast as actions
import gamepad

import logging
from logging import debug, warning
from PyObjCTools import AppHelper
import rumps

BUTTON_MUTE = 1
BUTTON_VIDEO = 2

class MuteButtonApp(rumps.App):
  def __init__(self):
    super(MuteButtonApp, self).__init__("Tyst")
    self.icon = "icon.icns"
    self.quit_button = None
    self.menu = ["Teams: Mute", "Quit"]
    self.gamepad_mgr = gamepad.GamepadManager(self.button_handler,
        gamepad_added=self.device_added,
        gamepad_removed=self.device_removed)

    self.devs_menu = rumps.MenuItem("Devices")
    self.menu.add(self.devs_menu)

  def device_added(self, gamepad):
    AppHelper.callAfter(self.add_dev_menu_item, gamepad)

  def device_removed(self, gamepad):
    AppHelper.callAfter(self.remove_dev_menu_item, gamepad)

  def add_dev_menu_item(self, gamepad):
    def callback(item):
      if item.state == 1:
        item.state = 0
        gamepad.close()
      else:
        item.state = 1
        gamepad.open()

    key = self.get_gamepad_key(gamepad)
    debug("Adding menu item '%s'", key)
    item = rumps.MenuItem(key)
    item.set_callback(callback)
    item.state = 1
    # TODO: should we keep the items sorted?
    self.devs_menu.add(item)
    item.title = f"{gamepad.manufacturer_string} {gamepad.product_string}"

  def remove_dev_menu_item(self, gamepad):
    key = self.get_gamepad_key(gamepad)
    debug("Removing menu item '%s'", key)
    self.devs_menu.pop(key)

  def get_gamepad_key(self, gamepad):
    return f"{gamepad.vendor_id:04x}:{gamepad.product_id:04x}"

  @rumps.clicked('Quit')
  def clean_up_before_quit(self, _):
    debug("Quitting")
    self.gamepad_mgr.close()
    rumps.quit_application()

  @rumps.clicked('Teams: Mute')
  def teams_mute(self, _):
    self.ms_teams_mute()

  def button_handler(self, button):
    debug(f"Button {button} pressed")
    if button == BUTTON_MUTE:
      AppHelper.callAfter(self.ms_teams_mute)
    elif button == BUTTON_VIDEO:
      AppHelper.callAfter(self.ms_teams_video)

  def ms_teams_mute(self):
    debug("Muting Teams")
    try:
      actions.ms_teams_mute()
    except Exception as err:
      logging.exception("Failed to mute Microsoft Teams")
      rumps.alert(title="Error", message=str(err))

  def ms_teams_video(self):
    debug("Toggling Teams video")
    try:
      actions.ms_teams_video()
    except Exception as err:
      logging.exception("Failed to toggle Microsoft Teams video")
      rumps.alert(title="Error", message=str(err))

  def start(self):
    logging.critical("Tyst starting")
    trusted = accessibility.isTrustedWithPrompt()
    if not trusted:
      warning("Accessibility control is not enabled for the app")
    self.run()

if __name__ == '__main__':
  logHandlers = [logging.StreamHandler()]
  logging.basicConfig(level=logging.DEBUG,format="%(levelname)s:%(threadName)s:%(message)s", handlers=logHandlers)
  rumps.debug_mode(True)
  app = MuteButtonApp()
  app.start()
