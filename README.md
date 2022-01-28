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

* Install rumps (needed to make a status bar app)

```
pip3 install -U rumps --user
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

* Enable "System Events" access for Tyst

* Allow Accessibility access for Tyst
