import applescript
from logging import info
import os

ms_teams_mute_scpt = applescript.AppleScript(path="microsoft-teams-mute.applescript")

def ms_teams_mute():
  ms_teams_mute_scpt.run()
