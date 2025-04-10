import pygame
import random

class Enemy:
    def __init__(self, x, y, sprite_path, speed=2, points=10):
        self.x = x
        self.y = y
        self.speed = speed
        self.points = points
        self.sprite = pygame.image.load(sprite_path)

    def move(self):
        self.y += self.speed
        if random.randint(0, 5) == 0:
            self.x += self.speed
            if random.randint(0, 1) == 0:
                self.x -= self.speed * 5
            else:
                self.x += self.speed * 5
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))