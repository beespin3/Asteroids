import pygame
import circleshape
from constants import PLAYER_SHOOT_SPEED

SHOT_RADIUS = 5

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
         super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt