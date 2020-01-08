import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(color)

    def move(self):
        pass
