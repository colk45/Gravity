import pygame, sys
from pygame.math import Vector2 as Vector
from Planet import Planet, planets

last_mouse_pos = Vector(0, 0)
first_mouse_pos = Vector(0, 0)

clock = pygame.time.Clock()
FPS = 60

pygame.init()

WIDTH, HEIGH = 0, 0
screen = pygame.display.set_mode((WIDTH, HEIGH), pygame.FULLSCREEN)
WIDTH, HEIGH  = screen.get_size()

LIGHT_GREY = pygame.Color('grey12')

planet = Planet((0, 0), 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()   

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            planet.create()
            if len(planets) > 0: 
                planets[-1].velocity = Vector(mouse_velocity_x, mouse_velocity_y) / 4

    screen.fill(LIGHT_GREY)

    mouse_velocity_x, mouse_velocity_y = pygame.mouse.get_rel()

    # planet physics
    for planet_i in planets:
        planet_i.update()
        
    planet.draw()

    pygame.display.update()
    clock.tick(FPS)
