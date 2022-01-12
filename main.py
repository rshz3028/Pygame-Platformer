import pygame,os,sys
from pygame.locals import *

from settings import *
from level import Level

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def main():
    
    pygame.init()

    SCREENRECT = Rect(0,0,screen_width,screen_height)
    fullscreen = False

    winstyle = 0
    best_depth = pygame.display.mode_ok(SCREENRECT.size,winstyle,32)
    screen = pygame.display.set_mode(SCREENRECT.size,winstyle,best_depth)

    clock = pygame.time.Clock()

    level = Level(level_map,screen)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit();sys.exit()

        screen.fill(BLACK)

        level.run()
        
        clock.tick(60)
        pygame.display.update()

if __name__ == '__main__':
    main()
