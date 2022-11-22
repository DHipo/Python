import os
from Const import surf, sizeScreen, draw, pygame

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, n = 'null', c = (0,0,0), h = int, a = 0, o = 'null', at = {"attack1":{"damage":0, "name":'null'}},sName = 'null', p = {"x": 0, "y":0}, s = {"x": 50, "y":50}) -> None:
        super().__init__()
        self.color = c 
        self.owner = o
        self.name = n
        self.position = p
        self.size = s
        self.health = h
        self.TotalHealth = h
        self.attack = a
        self.attacks = at
        #self.RectP = pygame.Rect(70,(sizeScreen[1]/3) + 40, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"])
        #self.RectE = pygame.Rect(((sizeScreen[0]/3) * 2)-20,20, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"])
        self.path = os.path.realpath('..\Python\Pokemon (sprites)\Img\\'+ sName)
        self.Oimage = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.Oimage, (250,250))
        self.rect = self.image.get_rect()
        pass

    def DrawSprite(self):
        if self.owner == 'Player':
            self.rect = [90,(sizeScreen[1]/3) + 40, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]]
            #draw.rect(surf, self.color,(70,(sizeScreen[1]/3) + 40, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]), 0, 10)
        #if self.owner == 'Enemy':
        else:
            self.rect = [((sizeScreen[0]/3) * 2)-20,20, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]]
            #draw.rect(surf, self.color,(((sizeScreen[0]/3) * 2)-20,20, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]), 0, 10)
    
    def Hit(self):
        if self.owner == 'Player': 
            for i in range(10):
                self.RectP.top -= 10
                draw.rect(surf, self.color,self.RectP, 0, 10)
            for i in range(10):
                self.RectP.top += 10
                draw.rect(surf, self.color, self.RectP, 0, 10)
        
        #if self.owner == 'Enemy': 
        else:
            for i in range(10):
                self.RectE.top -= 10
                draw.rect(surf, self.color, self.RectE, 0, 10)
            for i in range(10):
                self.RectE.top += 10
                draw.rect(surf, self.color, self.RectE, 0, 10)

class Background(pygame.sprite.Sprite):
    def __init__(self, scale = pygame.math.Vector2(1000,1000), po = pygame.math.Vector2(-1000,-100), name = 'null') -> None:
        super().__init__()
        #os.chdir('/../../../Programacion/LE/Python/Pokemon (sprites)/Img')
        self.path = os.path.realpath('..\Python\Pokemon (sprites)\Img\\'+ name)
        self.Oimage = pygame.image.load(self.path)
        self.scale = scale
        self.image = pygame.transform.scale(self.Oimage, (scale.x, scale.y))
        self.position = pygame.math.Vector2(po.x,po.y)
        self.rect = self.image.get_rect()
        self.rect = [self.position.x, self.position.y]
        self.movement = True
        self.state = 'free'
        self.id = 'background'

    def Update(self):
        self.rect = [self.position.x, self.position.y]

class Player(pygame.sprite.Sprite):    
    def __init__(self, c, p = pygame.math.Vector2(), s = pygame.math.Vector2(50,100), po = Pokemon , name = 'null') -> None:
        super().__init__()
        
        ##os.chdir('/../../../Programacion/LE/Python/Pokemon (sprites)/Img')
        self.path = os.path.realpath('..\Python\Pokemon (sprites)\Img\\'+ name)
        self.color = c 
        self.position = p
        self.movement = True
        self.state = 'free'
        self.pokemon = po
        self.pokemon.owner = 'Player'
        self.turn = True
        self.OriginalImage = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.OriginalImage, (100,131))
        self.rect = self.image.get_rect()
        self.rect.center = [50,65]
        self.rect.topleft = [sizeScreen[0]/2,sizeScreen[1]/2]
        self.size = self.rect.size
        self.id = 'player'
        pass

    def BoxCollider(self):
        pygame.draw.rect(surf, (0,0,0), self.rect)

class Enemy(pygame.sprite.Sprite):    
    def __init__(self, c, p = pygame.math.Vector2(), name = 'null', po = Pokemon, s = pygame.math.Vector2(50,100), r = pygame.math.Vector2(70,70)) -> None:
        super().__init__()
        
        self.path = os.path.realpath('..\Python\Pokemon (sprites)\Img\\'+ name)
        self.color = c 
        self.id = 'enemy'
        self.position = p
        self.state = 'free'
        self.movement = True
        self.size = s 
        self.radius = r
        self.pokemon = po
        self.turn = False
        self.OriginalImage = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.OriginalImage, (100,131))
        self.rect = self.image.get_rect()
        self.rect.center = [50, 65]

        self.BoxRadiusCollider = pygame.Rect(self.position.x-(self.radius.x/2), self.position.y-(self.radius.y/2), self.size.x + self.radius.x, self.size.y +self.radius.y)
        pass

    def Update(self):
        
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        self.BoxRadius()


    def BoxRadius(self):
        
        pygame.draw.rect(surf, (255,0,0), self.rect)
        #draw.rect(surf, (255,0,0,100), (self.position.x-(self.radius.x/2), self.position.y-(self.radius.y/2), self.size.x + self.radius.x, self.size.y +self.radius.y),0,10)


#Pokemons
Charizard = Pokemon('Charmander', (255,120,0), 300, 50,'Enemy', {
    "attack1":{
        "damage":10, 
        "name":'placaje'
        }, 
    "attack2":{
        "damage": 10, 
        "name": 'lanzallamas'
        }, 
    "attack3":{
        "damage": 10, 
        "name": 'vuelo'
        },  
    "attack4":{
        "damage": 10, 
        "name": 'fuego'
        }
    }, 'Charmander (Frente).png')

Pikachu = Pokemon('Pikachu', (255,255,0), 100, 20, 'Enemy', {
    "attack1":{
        "damage":10, 
        "name":'placaje'
        }, 
    "attack2":{
        "damage": 10, 
        "name": 'lanzallamas'
        }, 
    "attack3":{
        "damage": 10, 
        "name": 'vuelo'
        },  
    "attack4":{
        "damage": 10, 
        "name": 'fuego'
        }
    }, 'Pikachu (Espalda).png')

Bulbasaur = Pokemon('Bulbasaur', (0,150,60), 100, 20, 'Player', {
    "attack1":{
        "damage":10, 
        "name":'placaje'
        }, 
    "attack2":{
        "damage": 100, 
        "name": 'lanzallamas'
        }, 
    "attack3":{
        "damage": 100, 
        "name": 'vuelo'
        },  
    "attack4":{
        "damage": 10, 
        "name": 'fuego'
        }
    }, 'Bubasaur (Espalda).png')
