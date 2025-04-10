import pygame
from entities.bullet import Bullet

class Player:
    def __init__(self, x, y, sprite_path, bulletSpeed=7, speed=5, scoreMult=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.bulletSpeed = bulletSpeed
        self.scoreMult = scoreMult
        self.sprite = pygame.image.load(sprite_path)
    
    def move(self, keys, width):
        if keys[pygame.K_LEFT] and self.x > 0:  # Mover a la izquierda
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < width - 50:  # Mover a la derecha
            self.x += self.speed
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    
    def shoot(self):
        return Bullet(self.x + 20, self.y, self.bulletSpeed)