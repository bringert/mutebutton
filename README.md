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

* [Install Homebrew](https://brew.sh/)

* Fix permissions on /usr/local (seems stupid)

```
sudo chown -R $(whoami) $(brew --prefix)/*
```

* Install dependencies

```
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config
```

* Install pygame. Needs some architecture magic on macOS Monterey 12.1 on an Intel MacBook Pro.

```
export CC=/usr/bin/gcc
export CFLAGS='-arch i386 -arch x86_64'
export LDFLAGS='-arch i386 -arch x86_64'
export ARCHFLAGS='-arch i386 -arch x86_64'
python3 -m pip install -U pygame --user
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
