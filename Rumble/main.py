from random import randint, random
import re
import pygame, sys

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
pygame.display.init()

surf = pygame.display.set_mode((600,600))
screen = pygame.display
sizeScreen = pygame.display.get_window_size()
screen.set_caption("RUMBLE")

colorR = randint(0, 255)

rect = {
    'broken': False,
    'color': (0,0,0),
    'position': {
        'x': 0,
        'y': 0
    },
    'size': {
        'x': (sizeScreen[0] / 4)- 10,
        'y': 50
    }
}

rectPlayer = {
    'position': {
        'x': 0,
        'y': sizeScreen[1] - 100
    },
    'size': {
        'width': 150,
        'height': 10
    }, 
    'color': (255,255,255)
}

axisLH = 0

while 1:
    surf.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.JOYAXISMOTION:
            axisLH = joystick.get_axis(0)

    if axisLH > 0.5 or axisLH < -0.5:
        rectPlayer["position"]["x"] += axisLH
    
    for i in range(5):
        for a in range(4):
            rectB = pygame.rect.Rect((10 * a)+rect['size']['x'],(10 * i)+rect['size']['y'], rect["size"]["x"], rect["size"]["y"])
            pygame.draw.rect(surf, (colorR, colorR, colorR), rectB)

    screen.flip()