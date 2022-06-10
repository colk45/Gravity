import pygame, random, math
from pygame.math import Vector2 as Vector

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

G = 6.67408 * (10 ** -11)  # Gravitational Constant

class Particles:
    def __init__(self, position, radius):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.radius = radius
        self.position = Vector(position)  
        self.color = WHITE
        self.color_list = [(236, 114, 40), (93, 181, 241), (231, 147, 246)]
        self.image = pygame.draw.circle(self.surface, self.color, self.int_Vector(self.position), int(self.radius))
        self.particles = []
        
        self.velocity = Vector(0, 0)

        #gravity
        self.mass = 2 * 10**9 # kg

    def int_Vector(self, vector):
        return (int(vector.x), int(vector.y))
        
    def gravity_force(self):
        for particle in self.particles:
            self.position = Vector(self.position)
            dx = particle.position.x - self.position.x
            dy = particle.position.y - self.position.y
            distance = math.sqrt((dx)**2 + (dy)**2)
            if distance != 0:
                gravity = abs((G * particle.mass) / (distance**2))
                # angle between two particles
                angle = math.atan2(dy, dx)
                gravity_x = gravity * math.cos(angle)
                gravity_y = gravity * math.sin(angle)
                
                gravity = Vector(gravity_x, gravity_y)
                gravity = -gravity * 1000
                particle.velocity += gravity
                particle.position += particle.velocity

    def create(self):
        self.particles.append(Particles(self.position, self.radius))
        self.radius = 0
  
    def run(self):   
        self.gravity_force() 
         
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.radius += 0.4
            self.position = pygame.mouse.get_pos()
            Particles(self.position, self.radius)

        for particle in self.particles: 
            Particles(particle.position, particle.radius)
            

            
        


        

