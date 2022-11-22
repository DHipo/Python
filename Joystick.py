import pygame, sys
#Initialize the Joystick
pygame.joystick.init()
number = pygame.joystick.get_count()
print(number)
#Check if there is a joystick connected
joystick = pygame.joystick.Joystick(0)

pygame.display.init()

surf = pygame.display.set_mode((600,600))
screen = pygame.display
screen.set_caption("LE")

pygame.font.init()
font = pygame.font.SysFont('Calibri', 30)


axisLH, axisLV = 0, 0

player = {
    "positon": {
        'x': 0,
        'y': 0
    },
    "size": {
        'width': 50,
        'height': 150
    }
}

while 1:
    surf.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        #Button detection
        if event.type == pygame.JOYBUTTONDOWN:
            #Make rumble if button is pressed
            joystick.rumble(1,1,3)
            print(event.button)
        #Axis detection for left stick
        if event.type == pygame.JOYAXISMOTION:
            #Axis 0 is left stick's horizontal axis
            axisLH = joystick.get_axis(0)
            #Axis 1 is left stick's vertical axis
            axisLV = joystick.get_axis(1)
            #vibracion
            joystick.rumble(1,1,2)

    #Substract axis values to get player's position
    if axisLH > 0.5 or axisLH < -0.5:
        player["positon"]["x"] += axisLH

    if axisLV > 0.5 or axisLV < -0.5:
        player["positon"]["y"] += axisLV

    buttons = joystick.get_numbuttons()
    axes = joystick.get_numaxes()
    balls = joystick.get_numballs()
    
    #print the axis on the screen
    text = font.render(f'AxisLH: {axisLH}, AxisLV: {axisLV}', True, (255,255,255))
    surf.blit(text, (0,0))
    #print the player's position
    rect = pygame.rect.Rect((player['positon']['x'], player['positon']['y']), (player['size']['width'], player['size']['height']))
    pygame.draw.rect(surf,(255,255,255),rect)
    #Update the screen
    pygame.display.flip()
