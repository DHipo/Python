from xml.sax.handler import EntityResolver
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

Entity.default_shader = lit_with_shadows_shader                     

app = Ursina()
#piso
ground = Entity(model='plane', scale=10, texture='grass', collider='box')
#player
player = FirstPersonController(model='cube', color=color.red, speed=8)
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))

#obj
obj = Entity(model='sphere', scale=1.4, texture='brick', position=(0,2,1), collider='sphere')

directionLight = (0,0,0)
sun = DirectionalLight()

def Update():
    if held_keys['k']:
        directionLight += (.1,0,0)
        
    if held_keys['l']:
        directionLight += (0,-.1,0)
    
    
    sun.look_at(directionLight)

Sky()

app.run()