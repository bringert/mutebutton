* Reduce applescript latency first time it runs
  Maybe use pyobjc-framework-ScriptingBridge, bundle id com.microsoft.teams
  Or maybe send raw Apple Events using NSAppleEventDescriptor,
  like https://github.com/pyatom/pyatom/blob/master/atomac/AXClasses.py
  does with keypresses. To print Apple Events, from
  https://stackoverflow.com/questions/53638803/translate-into-apple-events-applescript

```
export AEDebugSends=1
osascript microsoft-teams-mute.applescript
```

* Improve device menu: persist device state, sort menu items alphabetically

* Run on Mac start-up, with a menu item to enable/disable
  https://stackoverflow.com/questions/3358410/programmatically-run-at-startup-on-mac-os-x

* Add About screen

* Connect to the Teams API to make it work without relying on the Teams app on the computer?
  https://docs.microsoft.com/en-us/graph/api/call-mute?view=graph-rest-1.0&tabs=http

* Build an enclosure for the hardware
