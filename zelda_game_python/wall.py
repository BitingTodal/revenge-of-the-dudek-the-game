import pygame
from setting import *

class Wall(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\gusta\Desktop\zelda_game_python/graphics/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,26)