import pygame
import sys

view_in = []

def renderer(view_from_ray_cast: int = []):
    #terminal_debug(view_in)
    global view_in
    view_in = view_from_ray_cast
    fish_eye_corg()
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    BLUE=(0,0,255)
    DISPLAY.fill((10,10,10))
    pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    return

def fish_eye_corg():
    global view_in
    return

def terminal_debug():
    global view_in
    for x in range(len(view_in)):
        print(view_in[x])
    return