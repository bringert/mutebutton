# pip3 install -U pyobjc-framework-ScriptingBridge --user
from ScriptingBridge import SBApplication

#teams = SBApplication.applicationWithBundleIdentifier_("com.microsoft.teams")
#teams.activate()

#print(type(teams))

#print([f for f in dir(teams) if "activate" in f.lower()])

system = SBApplication.applicationWithBundleIdentifier_("com.apple.systemevents")

word = SBApplication.applicationWithBundleIdentifier_("com.microsoft.Word")

#print(dir(SBApplication))

# Looks like the SBApplication objects have no methods of the their own

print((list(set(dir(word)) - set(dir(SBApplication)))))

#print(type(system_events.processes()[0]))

#for f in dir(system):
#  print(f)
