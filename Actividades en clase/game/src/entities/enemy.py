import pygame

class Enemy:
    def __init__(self, x, y, sprite_path, speed=2):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = pygame.image.load(sprite_path)

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))