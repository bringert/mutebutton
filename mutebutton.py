import os
import pygame.joystick


MUTE_BUTTON = 1


def button_pressed(button):
  if button == MUTE_BUTTON:
    print("Toggling mute in Microsoft Teams")
    os.system('osascript microsoft-teams-mute.applescript')


class JoystickWatcher:
  def __init__(self, button_down=None):
    self.button_down = button_down
    self.running = True
    pygame.init()
    self.clock = pygame.time.Clock()

    self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in self.joysticks:
      joy.init()

  def handle_joystick_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        print("Quitting...")
        self.running = False
      elif event.type == pygame.JOYBUTTONDOWN:
        if self.button_down:
          self.button_down(event.button)

  def run(self):
    while self.running:
      self.handle_joystick_events()
      self.clock.tick(20)

if __name__ == '__main__':
  JoystickWatcher(button_down=button_pressed).run()
