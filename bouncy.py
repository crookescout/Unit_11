import pygame, sys
from pygame.locals import *
import circle

pygame.init()
main_surface = pygame.display.set_mode((500, 400), 0, 32)
main_surface.fill((255, 255, 255))

new_circle = circle.Circle(main_surface)
new_circle.rect.x = 250
new_circle.rect.y = 200
main_surface.blit(new_circle.image, new_circle.rect)

while True:
    main_surface.fill((255, 255, 255))
    new_circle.move()
    main_surface.blit(new_circle.image, new_circle.rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
