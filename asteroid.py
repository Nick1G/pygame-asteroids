import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        first_new_vector = self.velocity.rotate(new_angle)
        second_new_vector = self.velocity.rotate(-new_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_split_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_split_asteroid.velocity = first_new_vector * 1.2

        second_split_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_split_asteroid.velocity = second_new_vector * 1.2