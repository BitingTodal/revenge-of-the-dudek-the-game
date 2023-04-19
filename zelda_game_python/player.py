import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\gusta\Desktop\zelda_game_python/graphics/david.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-30)

        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.obstacle_sprites = obstacle_sprites
    
    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y  = -2
        elif keys[pygame.K_s]:
            self.direction.y  = 2
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x  = -2
        elif keys[pygame.K_d]:
            self.direction.x  = 2
        else:
            self.direction.x = 0

        if pygame.key.key_code("return") == pygame.K_RETURN:
            self.speed == 3

        else:
            self.speed == 2


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  #gå til høyre
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  #gå ned
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom



    def update(self):
        self.key_input()
        self.move(self.speed)