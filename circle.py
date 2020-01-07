import pygame

class Circle:

    def __init__(self, main_surface):

        self.main_surface = main_surface
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.x_speed = 3
        self.y_speed = 4

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left < 0 or self.rect.right > self.main_surface.get_width():
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.main_surface.get_height():
            self.y_speed = -self.y_speed
