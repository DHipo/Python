import sys
import pygame as pg

surf = pg.display.set_mode((1000,600), 0 , 32)
screen = pg.display

pg.font.init()

font = pg.font.SysFont('Arial', 30)
times, timesO = 1, 1
text_input = ''
old_text = []
def printKeyPressed():
    global font, times, text_input, timesO
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            for key in keys:
                if key == True:
                    print(event.key)
                    text_input+=event.unicode
                    text = font.render(event.unicode, True, (0,255,0))
                    textRect = text.get_rect()
                    textRect.center = (0, 570)
                    textRect.x += times * 20
                    surf.blit(text, textRect)
                    times +=1
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == 13:
                surf.fill((0,0,0), (0,0,1000,600))
                old_text.append(text_input)
                print(old_text)
                timesO = 1
                for texto in old_text:
                    t = font.render(texto, True, (0,255,0))
                    tr = t.get_rect()
                    tr.topleft = (0,0)
                    tr.y += timesO * 30
                    
                    surf.blit(t, tr)
                    timesO +=1
                text_input = ''
                times = 1
        if event.type == pg.QUIT:
            sys.exit()

def main():
    while 1:
        printKeyPressed()

        screen.flip()

main()