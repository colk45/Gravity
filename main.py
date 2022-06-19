import pygame, sys, random
from Particles import Particles, particles

pygame.init()

SCREEN_SIZE = (1000, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)
LIGHT_GREY = pygame.Color('grey12')

clock = pygame.time.Clock()
FPS = 60

particle = Particles((0, 0), 0)

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
            particle.create()

    screen.fill(LIGHT_GREY)

    particle.draw()

    for particle_i in particles:
        particle_i.update()

    pygame.display.update()
    clock.tick(FPS)
        
