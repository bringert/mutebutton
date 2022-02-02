import actions
import gamepad

import logging
from logging import debug
from PyObjCTools import AppHelper
import rumps

BUTTON_MUTE = 1

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
    name = self.get_gamepad_name(gamepad)
    debug("Adding menu item '%s'", name)
    item = rumps.MenuItem(name)
    item.set_callback(self.dev_clicked)
    item.state = 1
    self.devs_menu.add(item)

  def remove_dev_menu_item(self, gamepad):
    name = self.get_gamepad_name(gamepad)
    debug("Removing menu item '%s'", name)
    self.devs_menu.pop(name)

  def get_gamepad_name(self, gamepad):
    return f"{gamepad.vendor_id:04x}:{gamepad.product_id:04x}"

  def dev_clicked(self, item):
    item.state = 0 if item.state == 1 else 1

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
  rumps.debug_mode(True)
  app = MuteButtonApp()
  app.run()
