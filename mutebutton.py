import os
import pygame.joystick


MUTE_BUTTON = 1

def button_pressed(button):
  if button == MUTE_BUTTON:
    print("Toggling mute in Microsoft Teams")
    os.system('osascript microsoft-teams-mute.applescript')


running = True

pygame.init()

clock = pygame.time.Clock()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joy in joysticks:
  joy.init()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Quitting...")
      running = False
    elif event.type == pygame.JOYBUTTONDOWN:
      button_pressed(event.button)
  clock.tick(20)

pygame.joystick.quit()
