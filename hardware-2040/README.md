Simple USB HID gamepad device that uses a single momentary pushbutton

# Raspberry Pi Pico version

## Hardware

* Raspberry Pi Pico

* Momentary pushbutton connected between GND and GP16

## Installation

* Install CircuityPython, see
  https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

* Copy code to Raspberry Pi Pico:

  ```
  cp boot.py hid_gamepad.py /Volumes/CIRCUITPY/
  cp code-rpi-pico.py /Volumes/CIRCUITPY/code.py
  ```

* Reset device to pick up new boot.py

# Pimoroni Tiny 2040 version

* Download CircuitPython from https://circuitpython.org/board/pimoroni_tiny2040/

* Copy .uf2 file to /Volumes/RPI-RP2

* Copy code to Tiny 2040:

```
cp boot.py hid_gamepad.py /Volumes/CIRCUITPY/
cp code-tiny-2040.py /Volumes/CIRCUITPY/code.py
```


# TODO: Arduino code version

Maybe try https://bestofcpp.com/repo/mikeneiderhauser-CRSFJoystick
