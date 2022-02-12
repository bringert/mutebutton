import board
import digitalio
import usb_hid
import time

import neopixel

import hid_gamepad

gp = hid_gamepad.Gamepad(usb_hid.devices)

def neokey_button(pin):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    return button

buttons = {1:neokey_button(board.GP12), 2:neokey_button(board.GP11)}

neopixel_pin = board.GP10

# Default pixel order is GRB
# This kills the button inputs for some reason
num_pixels = 2
#pixel = neopixel.NeoPixel(neopixel_pin, num_pixels, bpp=3)
#pixel[0] = (10, 0, 0)
#pixel[1] = (0, 0, 255)

print("Started")

buttons_values = {}

while True:
    new_buttons_values = {i: b.value for i,b in buttons.items()}
    gp.set_buttons(new_buttons_values)
    if new_buttons_values != buttons_values:
      buttons_values = new_buttons_values
      print("Button state: ", buttons_values)
    time.sleep(0.01)
