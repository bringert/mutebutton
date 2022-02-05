# pip3 install -U py-appscript --user
import appscript
import struct

def ms_teams_mute():
  appscript.app("Microsoft Teams").activate()
  appscript.app("System Events").keystroke('m', using=['Ksft','Kcmd'])

if __name__ == '__main__':
  ms_teams_mute()
