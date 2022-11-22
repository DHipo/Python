import pygame, sys, math

surf = pygame.display.set_mode((800,600), 0 , 32)

colors = {(0,0,0),(255,255,255)}

screen = pygame.display
screen.set_caption('Bandera de arg')

i=0

def drawLine(alpha):
    pygame.draw.line(surf, (255,255,0), (size[0]/2, size[1]/2), ((size[0]/2 + math.cos(alpha) * 200),(size[1]/2 + math.sin(alpha) * 200)), 10)
    pygame.draw.line(surf, (255,255,0), (size[0]/2, size[1]/2), ((size[0]/2 + math.cos(alpha*2) * 200),(size[1]/2 + math.sin(alpha*2) * 200)), 1)
    pygame.draw.line(surf, (255,255,0), (size[0]/2, size[1]/2), ((size[0]/2 + math.cos(alpha*3) * 200),(size[1]/2 + math.sin(alpha*3) * 200)), 5)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    size = screen.get_window_size()
    pygame.draw.rect(surf, (90,90,125),(0, 0,800,size[1]/3 ))
    
    pygame.draw.rect(surf, (255,255,255),(0,(size[1]/3)*1, 800, size[1]/3))
    
    pygame.draw.rect(surf, (90,90,125),(0,(size[1]/3)*2,800, size[1]/3))

    pygame.draw.circle(surf, (255,255,0),(size[0]/2, size[1]/2), 80)
    drawLine(i)
    screen.update()
    i+=10