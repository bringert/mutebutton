import gamepad

import os
import rumps
import threading
import time

BUTTON_MUTE = 1

class MuteButtonApp(object):
  def __init__(self):
    self.app = rumps.App("Mute test", icon="icon.icns")

  def watch_mute_buttons(self):
    for device in gamepad.find_joysticks_and_gamepads():
      thread = threading.Thread(target=gamepad.watch_mute_button, args=(device, self.button_handler), daemon=True)
      thread.start()

  def button_handler(self, button):
    if button == BUTTON_MUTE:
      print(f"Button {button} pressed")
      self.ms_teams_mute()

  def ms_teams_mute(self):
    print("Toggling mute in Microsoft Teams...")
    start_time = time.time()
    os.system('osascript microsoft-teams-mute.scpt')
    elapsed_time_ms = int(1000 * (time.time() - start_time))
    print(f"Muting mic took {elapsed_time_ms} ms")

  def run(self):
    self.watch_mute_buttons()
    self.app.run()

if __name__ == '__main__':
  app = MuteButtonApp()
  app.run()
