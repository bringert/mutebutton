Simple USB HID gamepad device that uses a single momentary pushbutton

# Hardware

* Raspberry Pi Pico, Tiny 2040 or other device that supports CircuitPython

* Momentary pushbutton connected between GND and GP16

# Installation

* Install CircuityPython, see
  https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

* Copy code to device:

```
cp boot.py code.py hid_gamepad.py /Volumes/CIRCUITPY/
```

* Reset device to pick up new boot.py
