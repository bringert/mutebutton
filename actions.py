from logging import info
import os

def ms_teams_mute():
  info("Toggling mute in Microsoft Teams...")
  os.system('osascript microsoft-teams-mute.scpt')
