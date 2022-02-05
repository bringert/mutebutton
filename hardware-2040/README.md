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
