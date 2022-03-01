# Toggles microphone mute in Microsoft Teams by sending Cmd-Shift-M to the
# Teams process using Quartz Event Services.
import accessibility

from AppKit import NSRunningApplication, NSWorkspace
from Quartz import CGEventCreateKeyboardEvent, CGEventSetFlags, CGEventPostToPid, kCGEventFlagMaskShift, kCGEventFlagMaskCommand
from logging import warning

# To bring Teams to the foreground, we can use
# tell application "Microsoft Teams"
#  reopen
#  activate
# end tell
#
# Apple Events generated:
# $ AEDebugSends=1 osascript microsoft-teams-mute.applescript
# {aevt,rapp target='psn '[Microsoft Teams] {} attr:{subj=NULL-impl,csig=65536} returnID=8710}
# {misc,actv target='psn '[Microsoft Teams] {} attr:{subj=NULL-impl,csig=65536} returnID=-9689}

def sendShiftCommandM():
  keyCodeM = 46
  cmdShift = kCGEventFlagMaskShift | kCGEventFlagMaskCommand
  sendKeystrokeToTeams(keyCodeM, cmdShift)

def sendShiftCommandO():
  keyCodeO = 31
  cmdShift = kCGEventFlagMaskShift | kCGEventFlagMaskCommand
  sendKeystrokeToTeams(keyCodeO, cmdShift)

def sendKeystrokeToTeams(keyCode, flagMask):
  teamsBundleID = 'com.microsoft.teams'
  sendKeystrokeToApp(teamsBundleID, keyCode, flagMask)

def getAppPid(bundleID):
  for app in NSWorkspace.sharedWorkspace().runningApplications():
    if app.bundleIdentifier() == bundleID:
      return app.processIdentifier()
  return None

def sendKeystrokeToApp(appBundleID, keyCode, modifiers):
  if not accessibility.isTrustedWithPrompt():
    warning("Accessibility is not enabled")
    return

  pid = getAppPid(appBundleID)
  if not pid:
    # App is not running
    return

  keyDown = CGEventCreateKeyboardEvent(None, keyCode, True)
  CGEventSetFlags(keyDown, modifiers)
  keyUp = CGEventCreateKeyboardEvent(None, keyCode, False)
  CGEventSetFlags(keyUp, modifiers)

  # TODO: this doesn't seem to fail or print any error message if we don't
  # have the necessary privacy permission
  CGEventPostToPid(pid, keyDown)
  CGEventPostToPid(pid, keyUp)
  # We could also use CGEventPost to send it to the foreground app,
  # but then we'd have to bring the app to the foreground first
  #Quartz.CGEventPost(Quartz.kCGHIDEventTap, keyDown)
  #Quartz.CGEventPost(Quartz.kCGHIDEventTap, keyUp)

def ms_teams_mute():
  sendShiftCommandM()

def ms_teams_video():
  sendShiftCommandO()

if __name__ == '__main__':
  ms_teams_mute()
