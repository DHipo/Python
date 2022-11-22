from time import sleep
from Const import *
from Clases import *
from Movement import *
from FightState import *

player = Player(blue, pygame.math.Vector2((sizeScreen[0]/2)-25 , (sizeScreen[1]/2)- 50), pygame.math.Vector2(50, 100), Bulbasaur, 'Player.png')
enemy = Enemy(yellow, pygame.math.Vector2((sizeScreen[0]/2)-25, (sizeScreen[1]/2)-50), 'Player.png', Charizard)
enemy2 = Enemy(white, pygame.math.Vector2((sizeScreen[0]/2)+350, (sizeScreen[1]/2)-150), 'Player.png', Pikachu)

MapImage = Background(pygame.math.Vector2(4500,4500), pygame.math.Vector2(-200,-200),'Mapa.png')

ElementsS = pygame.sprite.Group()
ElementsS.add(MapImage)
ElementsS.add(enemy2)
ElementsS.add(enemy)
ElementsS.add(player)

Elements = [enemy, enemy2, MapImage]
Enemys = [enemy, enemy2]

while 1: 
    #pygame.draw.rect(surf, white, (0,0,sizeScreen[0], sizeScreen[1]))
    CheckExit()
    MapImage.Update()
    for enemy in Enemys:
        enemy.Update()

    #player.DrawSprite()
    ElementsS.draw(surf)
    #player.BoxCollider()
    Movement(Elements)
    keys = pygame.key.get_pressed()
    player.movement = True

    match player.state:
        case 'fight':
            for enemy in Enemys:
                if enemy.state == 'fight':
                    Fight(player, enemy)
                    screen.flip()

        case 'free':
            for enemy in Enemys:
                if enemy.rect.colliderect(player.rect) == True and player.state == 'free':
                    text = font.render("Press \"Y\" to fight (" + enemy.pokemon.name + ")", True, (0,0,0))
                    surf.blit(text, ((sizeScreen[0]/2)-100, ((sizeScreen[1]/3)*2)+20))
                    if keys[pygame.K_y]:
                        player.state = 'chat'
                        while player.state == 'chat':
                            pygame.draw.rect(surf, (128,128,128), (10,((sizeScreen[1]/3)*2), sizeScreen[0] - 20, ((sizeScreen[1]/3)-20)), 0,10)
                            player.movement = False
                            pygame.display.flip()
                            #sleep(1)
                            player.state = 'fight'
                            enemy.state = 'fight'
    
                screen.flip()