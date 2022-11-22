from Const import *
from DisplayInMenu import MoveDisplay, DrawDisplay, DrawHealthBars
from Clases import Background

background = Background(pygame.math.Vector2(1285, 720), pygame.math.Vector2(-3,-100), 'backgroundFight.png')

def Fight(Player, Enemy):
    grupPokemons = pygame.sprite.Group()
    grupPokemons.add(background)
    grupPokemons.add(Player.pokemon)
    grupPokemons.add(Enemy.pokemon)

    #clean the screen
    #surf.fill(white)

    #Display the Pokemons
    Player.pokemon.DrawSprite()
    Enemy.pokemon.DrawSprite()
    
    grupPokemons.draw(surf)

    #Look at the health to see if someone die
    CheckPokemonsLife(Player, Enemy)

    #Display Health Bars
    DrawHealthBars(Player.pokemon, Enemy.pokemon)

    #the bottom menu on the fight
    MenuFight(Player, Enemy)

def CheckPokemonsLife(Player, Enemy):
    if Player.pokemon.health <= 0:
        text = font.render("You lose!", True, (128,128,128))
        surf.blit(text, (sizeScreen[0]/2 - 100, sizeScreen[1]/2))
        pygame.display.update()
        time.sleep(2)

        Player.state = 'free'
        Player.movement = True
        Enemy.movement = True
        Menu["OptionS"]["name"] = 'Main'
        Menu["Times"] = 0
    
    if Enemy.pokemon.health <= 0:
        text = font.render("You win!", True, (128,128,128))
        surf.blit(text, (sizeScreen[0]/2 - 100, sizeScreen[1]/2))
        pygame.display.update()
        time.sleep(2)
        
        Player.state = 'free'
        Player.movement = True
        Menu["OptionS"]["name"] = 'Main'
        Menu["Times"] = 0

def MenuFight(Player, Enemy):
    global Menu
    if Player.turn:
        #HUD
        DrawDisplay(Player, Menu)
        #To move the pointer on the menu
        MoveDisplay()
        #Menu
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            match Menu["OptionS"]["name"]:
                case 'Main':
                    match Menu["OptionS"]["index"]:
                        case 0: 
                            Menu["OptionS"]["name"]  = 'fight'
                            time.sleep(0.1)
                        case 1:
                            Menu["OptionS"]["name"]  = 'mochila'

                        case 2:
                            Menu["OptionS"]["name"]  = 'pokemons'

                        case 3:
                            Menu["OptionS"]["name"] = 'huir'

                case 'fight':
                    if pygame.key.get_pressed()[pygame.K_LALT]:
                        Menu["OptionS"]["name"] = 'Main'
                    match Menu["OptionS"]["index"]:
                        case 0:
                            Enemy.pokemon.health -= Player.pokemon.attacks["attack1"]["damage"]
                            #Enemy.pokemon.Hit()

                        case 1:
                            Enemy.pokemon.health -= Player.pokemon.attacks["attack2"]["damage"]
                            #Enemy.pokemon.Hit()

                        case 2:
                            Enemy.pokemon.health -= Player.pokemon.attacks["attack3"]["damage"]
                            #Enemy.pokemon.Hit()

                        case 3:
                            Enemy.pokemon.health -= Player.pokemon.attacks["attack4"]["damage"]
                            #Enemy.pokemon.Hit()

                    Player.turn = False
                    #time.sleep(1)

                case 'huir': 
                    Player.state = 'free'
                    Player.movement = False
                    Enemy.state = 'free'

                    Menu["OptionS"]["name"] = 'Main'
                    Menu["Times"] = 0
    
    else: 
        damage = (Enemy.pokemon.attack + random.randint(1,20))
        Player.pokemon.health -= damage
        text = font.render('the enemy s damage was ' + str(damage), True, (128,128,128))
        surf.blit(text, (40,(sizeScreen[1]/3)*2))
        time.sleep(1)
        Player.turn = True


def DisplayMovement(Player, Enemy):

    #clean the menu
    pygame.draw.rect(surf, (128,128,128), (10,((sizeScreen[1]/3)*2), sizeScreen[0] - 20, ((sizeScreen[1]/3)-20)), 0,10)
    #and display the name of the attack
    pygame.draw.rect(surf, (128,0,128), (20,((sizeScreen[1]/3)*2)+10, sizeScreen[0] - 230, ((sizeScreen[1]/3)-30)), 0,10)