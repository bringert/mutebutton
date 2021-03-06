# USB mute button for Microsoft Teams on Mac

## Hardware

Any USB HID joystick or gamepad should be supported.

To build your own with an Arduino Micro or other 32u4 device, see
[joyhandbrake](https://github.com/bringert/joyhandbrake).

To build your own with a Raspberry Pi Pico, or other RP2040 device, see
[hardware-2040](hardware-2040).

## Mac software dependencies

* Install python-libusb1

```
brew install libusb1
pip3 install -U libusb1 --user
```

* Install hidapi

```
pip3 install -U hidapi --user
```

* Install rumps (needed to make a status bar app)

```
pip3 install -U rumps --user
```

* Install the Quartz framework bindings to inject keypresses

```
pip3 install -U pyobjc-framework-ApplicationServices pyobjc-framework-CoreText pyobjc-framework-Quartz --user
```

* Install py-applescript to run the automation script

```
pip3 install -U py-applescript --user
```

## Running

```
python3 Tyst.py
```


## Building as a Mac app

* Install py2app

```
pip3 install -U py2app --user
```

* Build app (in development/alias mode)

```
python3 setup.py py2app -A
```

* Build app (in standalone mode)

```
python3 setup.py py2app
```

## Running as a mac app

* Run app:

```
open dist/Tyst.app
```

* Run app with console output:

```
dist/Tyst.app/Contents/MacOS/Tyst
```

* Allow Accessibility access for Tyst
