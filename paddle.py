import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        super().__init__()
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height

        # Create a surface with the correct height and width
        # self.image = pygame.Surface((width, height))

        # this makes the paddle a shooting star image
        self.image = pygame.image.load("s.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        # self.image.fill(color)

    def move(self, position):
        """
        This function makes the x coordinates of the paddle move with x coordinates of the mouse
        :param position:
        :return:
        """
        self.rect.x = position[0]


