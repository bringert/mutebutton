import gamepad

import threading
import time

def button_handler(button):
  print(f"Button {button} pressed")

if __name__ == '__main__':
  for device in gamepad.find_joysticks_and_gamepads():
    thread = threading.Thread(target=gamepad.watch_mute_button, args=(device, button_handler), daemon=True)
    thread.start()
  while True:
    time.sleep(0.1)
