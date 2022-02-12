Simple USB HID gamepad device that uses a single momentary pushbutton


# Raspberry Pi Pico version

## Hardware

* Raspberry Pi Pico

* Momentary pushbutton connected between GND and GP16

## Installation

* Download CircuityPython from https://circuitpython.org/board/raspberry_pi_pico/

* Copy .uf2 file to /Volumes/RPI-RP2

* Copy code to Raspberry Pi Pico:

```
cp boot.py hid_gamepad.py /Volumes/CIRCUITPY/
cp code-rpi-pico.py /Volumes/CIRCUITPY/code.py
```

* Reset device to pick up new boot.py


# Raspberry Pi Pico + NeoKey Featherwing version

## Hardware

* Raspberry Pi Pico

* Adafruit Neokey Featherwing. Pins on Neokey Featherwing connected as follows,
  with board key side up, text properly oriented:
  * 3rd pin from bottom right is NeoKey button A, connected to Pico GP12 (pin 16)
  * 4th pin from bottom right is NeoKey button B, connected to Pico GP11 (pin 15)
  * 5th pin from bottom right is NeoPixel Input, connected to Pico GP10 (pin 14)
  * 1st pin from bottom left is GND, connected to Pico GND (pin 23)
  * 2nd pin from top left is +3.3V, connected to Pico +3.3V (pin 36), by bridging
    to Neokey 3rd pin from top left


## Installation

* Download CircuityPython from https://circuitpython.org/board/raspberry_pi_pico/

* Copy .uf2 file to /Volumes/RPI-RP2

* Download Circuit Python mpy bundle from https://circuitpython.org/libraries and
  copy lib/neopixel.mpy to /Volumes/CIRCUITPY/lib:

```
curl -L https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20220212/adafruit-circuitpython-bundle-7.x-mpy-20220212.zip | tar -Oxf - adafruit-circuitpython-bundle-7.x-mpy-20220212/lib/neopixel.mpy > /Volumes/CIRCUITPY/lib/neopixel.mpy
```

* Copy code to Raspberry Pi Pico:

```
cp boot.py hid_gamepad.py /Volumes/CIRCUITPY/
cp code-rpi-pico-neokey-featherwing.py /Volumes/CIRCUITPY/code.py
```

* Reset device to pick up new boot.py


# Pimoroni Tiny 2040 version

## Hardware

* Pimoroni Tiny 2040, https://shop.pimoroni.com/products/tiny-2040

* Momentary pushbutton connected between +3.3V and GP4

## Installation

* Download CircuitPython from https://circuitpython.org/board/pimoroni_tiny2040/

* Copy .uf2 file to /Volumes/RPI-RP2

* Copy code to Tiny 2040:

```
cp boot.py hid_gamepad.py /Volumes/CIRCUITPY/
cp code-tiny-2040.py /Volumes/CIRCUITPY/code.py
```


# TODO: Arduino code version

Maybe try https://bestofcpp.com/repo/mikeneiderhauser-CRSFJoystick
