from Clases import Pokemon
from Const import *

offset = {
    "x": 80,
    "y": 30
}

sizeRect = {
    "x": sizeScreen[0]-100,
    "y": ((sizeScreen[1]/3)/2)
}

def MoveDisplay():
    global Menu, key
    #get the key pressed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = event.key
        else:
            if event.type == pygame.KEYUP:
                key = 0
        if event.type == pygame.K_ESCAPE:
            sys.exit()

    match Menu["OptionS"]["name"]:
        case 'Main' | 'fight':
            #right
            if key == pygame.K_d and (Menu["OptionS"]["index"] == 0 or Menu["OptionS"]["index"] == 2):
                Menu["OptionS"]["index"]+=1
            #down
            if key == pygame.K_s and (Menu["OptionS"]["index"] == 0 or Menu["OptionS"]["index"] == 1):
                Menu["OptionS"]["index"]+=2
            #up
            if key == pygame.K_w and (Menu["OptionS"]["index"] == 2 or Menu["OptionS"]["index"] == 3):
                Menu["OptionS"]["index"]-=2
            #left
            if key == pygame.K_a and (Menu["OptionS"]["index"] == 1 or Menu["OptionS"]["index"] == 3):
                Menu["OptionS"]["index"]-=1
        case 'fight':
            if key == pygame.K_LALT and (Menu["OptionS"]["name"]  == 'fight' or Menu["OptionS"]["name"]  == 'pokemon'):
                Menu["OptionS"]["name"]  = 'Main'

        case 'pokemons':
            #up
            if key == pygame.K_s and (Menu["OptionS"]["index"] >= 0 and Menu["OptionS"]["index"] < 3):
                Menu["OptionS"]["index"] += 1
                time.sleep(0.1)
            #down
            if key == pygame.K_w and (Menu["OptionS"]["index"] > 0 and Menu["OptionS"]["index"] <= 3):
                Menu["OptionS"]["index"] -= 1
                time.sleep(0.1)
            #back
            if key == pygame.K_LALT and (Menu["OptionS"]["name"]  == 'fight' or Menu["OptionS"]["name"]  == 'pokemon'):
                Menu["OptionS"]["name"]  = 'Main'

def DrawDisplay(Player, menu):

    #Options to select
    pygame.draw.rect(surf, (128,128,128), (10,((sizeScreen[1]/3)*2), sizeScreen[0] - 20, ((sizeScreen[1]/3)-20)), 0,10)

    #Left side of the menu
    InfoR = pygame.Rect(20,((sizeScreen[1]/3)*2)+10,(sizeScreen[0]/2)-20,(sizeScreen[1]/3)-40)
    pygame.draw.rect(surf, (255,255,0), InfoR, 0 ,10)


    #Right side of the menu - 4
    SelecR0 = pygame.Rect((sizeScreen[0]/2)+10, ((sizeScreen[1]/3)*2)+20, Menu["x"]-30, Menu["y"]-40)
    SelecR1 = pygame.Rect((sizeScreen[0]/2)+10, ((sizeScreen[1]/3)*2)+((sizeScreen[1]/3)/2), Menu["x"]-30, Menu["y"]-40)
    SelecR2 = pygame.Rect((sizeScreen[0]/2)+(sizeScreen[0]/2)/2+10, ((sizeScreen[1]/3)*2)+20, Menu["x"]-30, Menu["y"]-40)
    SelecR3 = pygame.Rect((sizeScreen[0]/2)+(sizeScreen[0]/2)/2+10, ((sizeScreen[1]/3)*2)+((sizeScreen[1]/3)/2), Menu["x"]-30, Menu["y"]-40)
    
    RectSelec = [SelecR0, SelecR2, SelecR1, SelecR3]
    
    for rect in RectSelec:
        pygame.draw.rect(surf, Menu["color"], rect, 0,10)

    
    #Pointer
    pygame.draw.rect(surf, Menu["colorS"], (RectSelec[Menu["OptionS"]["index"]].left, RectSelec[Menu["OptionS"]["index"]].top,  Menu["x"]-30, Menu["y"]-40), 0,10)

    match menu["OptionS"]["name"]:
        case 'Main':
            #display text
            f = pygame.font.SysFont('Calibri', 30)
            text = f.render('Fight', True, (0,0,0))
            textR = text.get_rect(center=(SelecR0.left + offset["x"], SelecR0.top + offset["y"]))
            surf.blit(text, textR)

            text = f.render('Mochila', True, (0,0,0))
            textR = text.get_rect(center=(SelecR2.left + offset["x"], SelecR2.top + offset["y"]))
            surf.blit(text, textR)

            text = f.render('Huir', True, (0,0,0))
            textR = text.get_rect(center=(SelecR3.left + offset["x"], SelecR3.top + offset["y"]))
            surf.blit(text, textR)

            text = f.render('Pokemon', True, (0,0,0))
            textR = text.get_rect(center=(SelecR1.left + offset["x"], SelecR1.top + offset["y"]))
            surf.blit(text, textR)
        case 'fight':
            #display attacks
            f = pygame.font.SysFont('Calibri', 30)
            text = f.render(Player.pokemon.attacks["attack1"]["name"], True, (0,0,0))
            textR = text.get_rect(center=(SelecR0.left + offset["x"], SelecR0.top + offset["y"]))
            surf.blit(text, textR)
            text = f.render(Player.pokemon.attacks["attack2"]["name"], True, (0,0,0))
            textR = text.get_rect(center=(SelecR2.left + offset["x"], SelecR2.top + offset["y"]))
            surf.blit(text, textR)
            text = f.render(Player.pokemon.attacks["attack3"]["name"], True, (0,0,0))
            textR = text.get_rect(center=(SelecR3.left + offset["x"], SelecR3.top + offset["y"]))
            surf.blit(text, textR)
            text = f.render(Player.pokemon.attacks["attack4"]["name"], True, (0,0,0))
            textR = text.get_rect(center=(SelecR1.left + offset["x"], SelecR1.top + offset["y"]))
            surf.blit(text, textR)
        case 'pokemons':         
            surf.fill(white)
            rect1 = pygame.rect.Rect(50,50,sizeRect["x"], sizeRect["y"])
            rect2 = pygame.rect.Rect(50,sizeRect["y"]+70,sizeRect["x"], sizeRect["y"])
            rect3 = pygame.rect.Rect(50,sizeRect["y"]+190,sizeRect["x"], sizeRect["y"])
            rect4 = pygame.rect.Rect(50,sizeRect["y"]+310,sizeRect["x"], sizeRect["y"])
            rects = [rect1, rect2, rect3, rect4]
            for rect in rects:
                pygame.draw.rect(surf, (128,128,128), rect, 0, 10)
            pygame.draw.rect(surf, (200,200,200), rects[Menu["OptionS"]["index"]])


def DrawHealthBars(Pokemon1 = Pokemon, Pokemon2 = Pokemon):
    #Draw Obj1 Health Bar first - User1
    pygame.draw.rect(surf, (100,100,100),((sizeScreen[0]/3)*2,(sizeScreen[1]/3) + 50, (sizeScreen[0]/3)-20, (sizeScreen[1]/3)-80), 0, 10)
    pygame.draw.rect(surf, (0,255,0), (((sizeScreen[0]/3)*2) + 10,(sizeScreen[1]/3) + 130, ((sizeScreen[0]/3) - 40)*(Pokemon1.health/Pokemon1.TotalHealth), 20), 0, 20)
    
    #Draw the name
    f = pygame.font.SysFont('Calibri', 30)
    text = f.render(Pokemon1.name, True, (0,0,0))
    surf.blit(text, (((sizeScreen[0]/3)*2)+10,(sizeScreen[1]/3) + 60))

    #Display the health with numbers
    f = pygame.font.SysFont('Calibri', 20)
    text = f.render(str(Pokemon1.health) + '/' +str(Pokemon1.TotalHealth), True, (0,0,0))
    surf.blit(text, (((sizeScreen[0]/3)*2)+10,(sizeScreen[1]/3) + 90))

    #Draw Obj2 Health Bar - Enemy
    pygame.draw.rect(surf, (100,100,100),(20, 20, (sizeScreen[0]/3)-20, (sizeScreen[1]/3)-80), 0, 10)
    pygame.draw.rect(surf, (0,255,0), (30, 100, ((sizeScreen[0]/3)-40)*(Pokemon2.health/Pokemon2.TotalHealth), 20), 0, 20)

    #Draw the name
    f = pygame.font.SysFont('Calibri', 30)
    text = f.render(Pokemon2.name, True, (0,0,0))
    surf.blit(text, (30,30))

    #Display the health with numbers
    f = pygame.font.SysFont('Calibri', 20)
    text = f.render(str(Pokemon2.health) + '/' +str(Pokemon2.TotalHealth), True, (0,0,0))
    surf.blit(text, (30, 60))