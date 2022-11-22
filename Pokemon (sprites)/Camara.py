import pygame
from Const import MiddleScreen

class Camera:
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.offsetStuff = pygame.math.Vector2()

        self.surf = pygame.display.get_surface()

    def center_target(self, target):
        self.offset.x = target.position['x'] - MiddleScreen.x
        self.offset.y = target.position['y'] - MiddleScreen.y

    def draw(self, stuff):
        self.offsetStuff.y = stuff.position.y + self.offset.y
        self.offsetStuff.x = stuff.position.x + self.offset.x
        pygame.draw.rect(self.surf, stuff.color, (self.offsetStuff, stuff.size), 0, 10)
