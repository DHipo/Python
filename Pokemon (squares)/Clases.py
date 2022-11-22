from turtle import position, screensize
from Const import surf, sizeScreen, draw, pygame

class Pokemon:
    def __init__(self, n = 'null', c = (0,0,0), h = int, a = 0, o = 'null', at = {"attack1":{"damage":0, "name":'null'}}, p = {"x": 0, "y":0}, s = {"x": 50, "y":50}) -> None:
        self.color = c 
        self.owner = o
        self.name = n
        self.position = p
        self.size = s
        self.health = h
        self.TotalHealth = h
        self.attack = a
        self.attacks = at
        self.RectP = pygame.Rect(70,(sizeScreen[1]/3) + 40, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"])
        self.RectE = pygame.Rect(((sizeScreen[0]/3) * 2)-20,20, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"])
        pass

    def DrawSprite(self):
        if self.owner == 'Player':
            draw.rect(surf, self.color,(70,(sizeScreen[1]/3) + 40, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]), 0, 10)
        #if self.owner == 'Enemy':
        else:
            draw.rect(surf, self.color,(((sizeScreen[0]/3) * 2)-20,20, (sizeScreen[0]/3)-self.size["x"], (sizeScreen[1]/3)-self.size["y"]), 0, 10)
    
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


class Player:    
    def __init__(self, c, p = pygame.math.Vector2(), s = pygame.math.Vector2(50,100), po = Pokemon) -> None:
        self.color = c 
        self.position = p
        self.size = s
        self.movement = True
        self.state = 'free'
        self.pokemon = po
        self.pokemon.owner = 'Player'
        self.turn = True
        self.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        pass
    
    def DrawSprite(self):
        draw.rect(surf, self.color, (self.position.x,self.position.y,self.size.x,self.size.y), 0, 10)

class Enemy:    
    def __init__(self, c, p = pygame.math.Vector2(), po = Pokemon,s = pygame.math.Vector2(50,100), r = pygame.math.Vector2(100,100), camera = pygame.math.Vector2(10, 10)) -> None:
        self.color = c 
        self.position = p
        self.state = 'free'
        self.movement = True
        self.size = s 
        self.radius = r
        self.pokemon = po
        self.turn = False
        self.BoxRadiusCollider = pygame.Rect(self.position.x-(self.radius.x/2), self.position.y-(self.radius.y/2), self.size.x + self.radius.x, self.size.y +self.radius.y)
        self.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        pass

    def DrawSprite(self):
        draw.rect(surf, self.color, (self.position.x ,self.position.y,self.size.x,self.size.y), 0, 10)

    def Update(self):
        self.BoxRadius()
        self.DrawSprite()


    def BoxRadius(self):
        self.BoxRadiusCollider = pygame.Rect(self.position.x-(self.radius.x/2), self.position.y-(self.radius.y/2), self.size.x + self.radius.x, self.size.y +self.radius.y)
        #draw.rect(surf, (255,0,0,100), (self.position.x-(self.radius.x/2), self.position.y-(self.radius.y/2), self.size.x + self.radius.x, self.size.y +self.radius.y),0,10)


#Pokemons
Charizard = Pokemon('Charizard', (255,120,0), 300, 50,'Enemy', {
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
    })

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
    })

Bulbasaur = Pokemon('Bulbasaur', (0,150,60), 100, 20, 'Player', {
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
    })
