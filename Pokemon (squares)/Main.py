from time import sleep
from Const import *
from Clases import *
from Movement import *
from FightState import *

player = Player(blue, pygame.math.Vector2((sizeScreen[0]/2)-25 , (sizeScreen[1]/2)- 50), pygame.math.Vector2(50, 100), Bulbasaur)
enemy = Enemy(yellow, pygame.math.Vector2((sizeScreen[0]/2)-25, (sizeScreen[1]/2)-50), Pikachu)
enemy2 = Enemy(white, pygame.math.Vector2((sizeScreen[0]/2)-150, (sizeScreen[1]/2)-75), Charizard)

Elements = [enemy, enemy2]

while 1: 
    surf.fill((120,120,255))
    CheckExit()

    for element in Elements:
        element.Update()

    player.DrawSprite()
    Movement(Elements)
    keys = pygame.key.get_pressed()
    player.movement = True

    match player.state:
        case 'fight':
            for element in Elements:
                if element.state == 'fight':
                    Fight(player, element)
                    screen.flip()

        case 'free':
            for element in Elements:
                if element.BoxRadiusCollider.colliderect(player.position, player.size) == True and player.state == 'free':
                    text = font.render("Press \"Y\" to fight (" + element.pokemon.name + ")", True, (0,0,0))
                    surf.blit(text, ((sizeScreen[0]/2)-100, ((sizeScreen[1]/3)*2)+20))
                    if keys[pygame.K_y]:
                        player.state = 'chat'
                        while player.state == 'chat':
                            pygame.draw.rect(surf, (128,128,128), (10,((sizeScreen[1]/3)*2), sizeScreen[0] - 20, ((sizeScreen[1]/3)-20)), 0,10)
                            player.movement = False
                            pygame.display.flip()
                            sleep(1)
                            player.state = 'fight'
                            element.state = 'fight'
            screen.flip()
