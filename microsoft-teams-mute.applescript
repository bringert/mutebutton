tell application "Microsoft Teams"
  reopen
  activate
end tell

# Requires enabling System Events control for Terminal / Tyst under
# System Preferences > Security & Privacy > Privacy > Automation
tell application "System Events" to keystroke "m" using {shift down, command down}
