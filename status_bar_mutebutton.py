import mutebutton

import rumps
import threading


# U+1F92B Shushing face / Face with Finger Covering Closed Lips
STATUS_BAR_EMOJI = "\U0001F92B"

class MuteButtonApp(object):
  def __init__(self):
    self.app = rumps.App("Mute test", STATUS_BAR_EMOJI)
    thread = threading.Thread(target=mutebutton.watch_mute_button, daemon=True)
    thread.start()

  def run(self):
    self.app.run()

if __name__ == '__main__':
  app = MuteButtonApp()
  app.run()
