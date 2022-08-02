import pygame, random, math
from pygame.math import Vector2 as Vector

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

G = 6.67408 * (10 ** -11)  # Gravitational Constant

SUPERFICIAL_DENSITY = 10**9 # d = m / s

planets = []

class Planet:
    def __init__(self, position, radius):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.WIDTH, self.HEIGH = self.surface.get_size()
        self.radius = radius
        self.position = Vector(position)  
        self.color = WHITE
        self.color_list = [(236, 114, 40), (93, 181, 241), (231, 147, 246)]
        self.image = pygame.draw.circle(self.surface, self.color, self.int_Vector(self.position), int(self.radius))
        self.collision_rect = pygame.Rect(self.position.x, self.position.y, self.radius, self.radius)

        self.velocity = Vector(0, 0)

        #gravity
        self.mass = int(SUPERFICIAL_DENSITY * math.pi * self.radius**2)

    def int_Vector(self, vector):
        return (int(vector.x), int(vector.y))
        
    def gravity_force(self):
        for planet in planets:
            distance_vector = self.position - planet.position

            dx = self.position.x - planet.position.x
            dy = self.position.y - planet.position.y

            distance = distance_vector.magnitude()
            if distance != 0 and distance_vector != (0, 0):
                gravity = G * planet.mass / distance**2
                theta = math.atan2(dy, dx) 
                gravity = -gravity
                gravity_vector = Vector(gravity*math.cos(theta),gravity*math.sin(theta))
                self.velocity += gravity_vector
        self.position += self.velocity
    
    def collision(self):
        for planet in planets:
            distance_vector = self.position - planet.position
            distance = distance_vector.magnitude()
            if self.radius > planet.radius and distance < self.radius:
                self.mass += planet.mass
                self.radius = int(math.sqrt(self.mass / (SUPERFICIAL_DENSITY * math.pi)))
                planets.remove(planet)
    
    def kill(self):
        for planet in planets:
            if planet.position.y < -60 or planet.position.y > self.HEIGH + 60:
                planets.remove(planet)
        
    def create(self):
        planets.append(Planet(self.position, self.radius))
        self.radius = 0

    def update(self):
        self.gravity_force()
        self.collision()
        self.kill()
  
    def draw(self):   
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.radius += 0.4
            self.position = pygame.mouse.get_pos()
            Planet(self.position, self.radius)
        
        for planet in planets: 
            Planet(planet.position, planet.radius)


        

