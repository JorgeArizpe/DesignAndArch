import pygame
from entities.player import Player

class PlayerBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.player = Player(0, 0, '../assets/images/player.png')
    
    def set_position(self, x, y):
        self.player.x = x
        self.player.y = y
    
    def set_speed(self, speed):
        self.player.speed = speed
    
    def set_bullet_speed(self, bullet_speed):
        self.player.bulletSpeed = bullet_speed
    
    def set_score_mult(self, score_mult):
        self.player.scoreMult = score_mult
    
    def get_player(self):
        player = self.player
        self.reset()
        return player