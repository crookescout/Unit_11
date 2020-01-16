import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        super().__init__()
        # initialize sprite super class

        # finish setting the class variables to the parameters
        self.color = color
        self.window_width = window_width
        self.window_height = window_height
        self.radius = radius

        self.sound = pygame.mixer.Sound('Pew_Pew.wav')

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        # self.image = pygame.Surface((radius, radius))
        # self.image.fill((255, 255, 255))
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        # pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5, 0)
        self.x_speed = 4
        self.y_speed = 3

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left < 0 or self.rect.right > self.window_width:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.y_speed = -self.y_speed

    def collide(self, sprite_group):
        if pygame.sprite.spritecollide(self, sprite_group, False):
            self.y_speed = -self.y_speed

    def collide_brick(self, sprite_group):
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.sound.play()
            self.y_speed = -self.y_speed
