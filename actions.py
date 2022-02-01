import applescript
from logging import info
import os

ms_teams_mute_scpt = applescript.AppleScript('''
tell application "Microsoft Teams" to activate

tell application "System Events" to keystroke "m" using {shift down, command down}
''')

def ms_teams_mute():
  ms_teams_mute_scpt.run()
