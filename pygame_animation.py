# Scout Crooke, 1/6/20, this program does pygame animtion

import pygame, sys
from pygame.locals import *


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption("Bouncing Ball")
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    x = 0
    y = 0
    speedx = 5
    speedy = 3
    block = pygame.Rect((x, y, 50, 50))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        main_surface.fill(WHITE)
        block.top += speedy
        block.left += speedx
        pygame.draw.rect(main_surface, RED, (block), 0)
        pygame.display.update()

main()