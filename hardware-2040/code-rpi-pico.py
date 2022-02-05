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

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Started")

while True:
    if not button.value:
        gp.press_buttons(gamepad_button_num)
        led.value = True
        print("Pressed")
    else:
        gp.release_buttons(gamepad_button_num)
        led.value = False
    time.sleep(0.1)
