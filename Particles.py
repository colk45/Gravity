import pygame, random, math
from pygame.math import Vector2 as Vector

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

G = 6.67408 * (10 ** -11)  # Gravitational Constant

SUPERFICIAL_DENSITY = 10**9 # d = m / s

particles = []

class Particles:
    def __init__(self, position, radius):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.radius = radius
        self.position = Vector(position)  
        self.color = WHITE
        self.color_list = [(236, 114, 40), (93, 181, 241), (231, 147, 246)]
        self.image = pygame.draw.circle(self.surface, self.color, self.int_Vector(self.position), int(self.radius))
        self.collision_rect = pygame.Rect(self.position.x, self.position.y, self.radius, self.radius)

        self.velocity = Vector(0, 0)

        #gravity
        self.mass = 0 # kg

    def int_Vector(self, vector):
        return (int(vector.x), int(vector.y))

    def mass_determination(self):
        self.mass = int(SUPERFICIAL_DENSITY * math.pi * self.radius**2)
        return self.mass
        
    def gravity_force(self):
        for particle in particles:
            particle.mass = particle.mass_determination()

            distance_vector = self.position - particle.position

            dx = self.position.x - particle.position.x
            dy = self.position.y - particle.position.y

            distance = distance_vector.magnitude()
            if distance != 0 and distance_vector != (0, 0):
                gravity = G * particle.mass / distance**2
                theta = math.atan2(dy, dx) 
                gravity = -gravity
                gravity_vector = Vector(gravity*math.cos(theta),gravity*math.sin(theta))
                self.velocity += gravity_vector
            self.position += self.velocity
    
    def collision(self):
        for particle in particles:
            distance_vector = self.position - particle.position
            distance = distance_vector.magnitude()
            if self.radius > particle.radius and distance < self.radius:
                self.mass += particle.mass
                self.radius = int(math.sqrt(self.mass / (SUPERFICIAL_DENSITY * math.pi)))
                particles.remove(particle)
                

    def create(self):
        particles.append(Particles(self.position, self.radius))
        self.radius = 0

    def update(self):
        self.gravity_force()
        self.collision()
  
    def draw(self):   
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.radius += 0.4
            self.position = pygame.mouse.get_pos()
            Particles(self.position, self.radius)

        for particle in particles: 
            Particles(particle.position, particle.radius)
            
        


        

