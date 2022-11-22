from Const import aceleration, pygame, BoxMap

def Movement(elements):
    for element in elements:

        if element.movement == True and element.state == 'free':
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                element.position.y += aceleration["y"]
            if keys[pygame.K_s]:
                element.position.y -= aceleration["y"]

            if keys[pygame.K_a]:
                element.position.x += aceleration["x"]

            if keys[pygame.K_d]:
                element.position.x -= aceleration["x"]