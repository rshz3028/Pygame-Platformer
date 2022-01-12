import pygame
from tiles import Tile
from settings import *
from player import Player

class Level:

    def __init__(self,level_data,surface):
        
        self.display_surface = surface
        self.setup(level_data)
        self.world_shift = 0

    def setup(self,layout):
        
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for ind,row in enumerate(layout):
            for col,cell in enumerate(row):
                x = col*tile_size
                y = ind*tile_size
                
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                    

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width*1/4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width*3/4 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_mov_colli(self):
        player = self.player.sprite
        player.rect.x += player.direction.x*player.speed
        
        for sprite in self.tiles.sprites():
            if player.rect.colliderect(sprite.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_mov_colli(self):
        player = self.player.sprite
        player.apply_gravity()
        player.rect.y += player.direction.y
        
        for sprite in self.tiles.sprites():
            if player.rect.colliderect(sprite.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                           
    def run(self):

        self.scroll_x()
        
        # Tile sprites
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player sprites
        self.player.update()
        self.horizontal_mov_colli()
        self.vertical_mov_colli()
        self.player.draw(self.display_surface)
        
    
