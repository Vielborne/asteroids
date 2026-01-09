import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw the asteroid to the given screen surface
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # Update asteroid position based on time passed this frame
    def update(self, dt):
        self.position += self.velocity * dt

    # Split this asteroid into two smaller, faster asteroids if it's big enough
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_asteroid_vector = self.velocity.rotate(random_angle)
            second_asteroid_vector = self.velocity.rotate(-random_angle)
            new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(
                self.position.x, self.position.y, new_asteroids_radius
            )
            second_asteroid = Asteroid(
                self.position.x, self.position.y, new_asteroids_radius
            )
            first_asteroid.velocity = first_asteroid_vector * 1.2
            second_asteroid.velocity = second_asteroid_vector * 1.2
