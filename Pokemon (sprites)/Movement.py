from Const import aceleration, pygame, sizeScreen

block = {
    "width": 0,
    "height": 0
}

def Movement(elements):
    
    global block

    for element in elements:

        #tengo que hacer que cuando le este sumando 0, osea que se choca contra la pared,
        #la posicion del jugador cambie

        if element.movement == True or element.state == 'free':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                match element.id:
                    case 'background':
                        if element.position.y >= 0:
                            element.position.y += 0
                            block["height"] = True
                        else:
                            element.position.y += aceleration["y"]
                            block["height"] = False
                    case 'enemy':
                        if block["height"]:
                            element.position.y += 0
                        else:
                            element.position.y += aceleration["y"]

            if keys[pygame.K_s]:
                match element.id:
                    case 'background':
                        if -element.position.y + sizeScreen[1] >= element.scale.y:
                            element.position.y += 0
                            block["height"] = True
                        else:
                            element.position.y -= aceleration["y"]
                            block["height"] = False
                    case 'enemy':
                        if block["height"]:
                            element.position.y += 0
                        else:
                            element.position.y -= aceleration["y"]

            if keys[pygame.K_a]:
                match element.id:
                    case 'background':
                        if element.position.x >= 0:
                            element.position.x += 0
                            block["width"] = True
                        else:
                            element.position.x += aceleration["x"]
                            block["width"] = False
                    case 'enemy':
                        if block["width"]:
                            element.position.y += 0
                        else:
                            element.position.x += aceleration["x"]

            if keys[pygame.K_d]:
                match element.id:
                    case 'background':
                        if -element.position.x + sizeScreen[0] >= element.scale.x :
                            element.position.x += 0
                            block["width"] = True
                        else:
                            element.position.x -= aceleration["x"]
                            block["width"] = False
                    case 'enemy':
                        if block["width"]:
                            element.position.x += 0
                        else:
                            element.position.x -= aceleration["x"]