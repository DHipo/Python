import pygame, sys, time, random

def CheckExit():
    #EXIT with the cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

pygame.font.init()

#camera
camera = {"x": 100, "y": 100}

#Screen
surf = pygame.display.set_mode((1280,720), 0, 32, 0, 1)
sizeScreen = pygame.display.get_window_size()
screen = pygame.display
screen.set_caption('Pokemon')
MiddleScreen = pygame.math.Vector2(sizeScreen[0] / 2, sizeScreen[1] / 2)

#Draw Function
draw = pygame.draw

#Font
font = pygame.font.SysFont('Arial', 30)

pygame.key.set_repeat(1)

#Aceleration
aceleration = {
    "x": 2.4,
    "y": 2.4
}

#Menu Options
Menu = {
    "x": (sizeScreen[0]/2)/2,
    "y": (sizeScreen[1]/3)/2,
    "color": (100,100,100),
    "colorS": (150,150,150),
    "OptionS": {
        "name":'Main', 
        "index":0
    },
    "times": 0
}

#Colors
white = (255,255,255)
red = (255, 0, 0)
yellow = (255,255,0)
orange = (255,128,0)
blue = (0,0,255)
brown = (100, 60, 30)

#Was pressed
key = 0
keys = 0

#Map
BoxMap = []