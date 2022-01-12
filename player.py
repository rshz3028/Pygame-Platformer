import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        
    
    def get_input(self):
        key = pygame.key.get_pressed()

        self.direction.x = key[K_RIGHT] - key[K_LEFT]
        if key[K_SPACE]:
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity

    def jump(self):
        self.direction.y = self.jump_speed
        
    def update(self):
        self.get_input()
        
       
        
