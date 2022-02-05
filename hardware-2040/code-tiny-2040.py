import board
import digitalio
import pwmio
import usb_hid
import time

import hid_gamepad

gp = hid_gamepad.Gamepad(usb_hid.devices)

gamepad_button_num = 2

button_pin = board.GP4

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

red = pwmio.PWMOut(board.LED_R, duty_cycle=65535)
green = pwmio.PWMOut(board.LED_G, duty_cycle=65535)
blue = pwmio.PWMOut(board.LED_B, duty_cycle=65535)

# Colors are 0-100
def led_rgb(r, g, b):
    red.duty_cycle = 65535 * (100 - r) // 100
    green.duty_cycle = 65535 * (100 - g) // 100
    blue.duty_cycle = 65535 * (100 - b) // 100

print("Started")

while True:
    if button.value:
        gp.press_buttons(gamepad_button_num)
        led_rgb(100, 0, 0)
        print("Pressed")
    else:
        gp.release_buttons(gamepad_button_num)
        led_rgb(0, 0, 0)
    time.sleep(0.01)

