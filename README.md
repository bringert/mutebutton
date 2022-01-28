# USB mute button for Microsoft Teams on Mac

## Hardware

* Arduino Pro Micro

* Momentary push button

## Firmware

[joyhandbrake](https://github.com/bringert/joyhandbrake)

## Mac software dependencies

* Test injecting mute events into Teams

```
osascript microsoft-teams-mute.applescript
```

* Install hidapi

```
pip3 install -U hidapi --user
```

## Running Mac software

```
python3 mutebutton.py
```


## Building stand-alone Mac app

* Install py2app

```
pip3 install -U py2app --user
```

* Build app (builds in alias mode)

```
python3 setup.py py2app -A
```

* Run app

* Enable "System Events" access for mutebutton

* Allow Accessibility access for mutebutton
