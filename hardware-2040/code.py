import board
import digitalio
import usb_hid
import time

import hid_gamepad

gp = hid_gamepad.Gamepad(usb_hid.devices)

gamepad_button_num = 2

button_pin = board.GP16

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print("Started")

while True:
    if not button.value:
        gp.press_buttons(gamepad_button_num)
        print("Pressed")
    else:
        gp.release_buttons(gamepad_button_num)
    time.sleep(0.1)
