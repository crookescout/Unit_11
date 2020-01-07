import pygame, sys
from pygame.locals import *
import brick

pygame.init()


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT))
    main_surface.fill((255, 255, 255))

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET

    for x in range(BRICKS_PER_ROW):
        my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, RED)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    y_pos = y_pos + BRICK_SEP + BRICK_HEIGHT
    for x in range(BRICKS_PER_ROW):
        my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, RED)
        main_surface.blit(my_brick.image, (x_pos, y_pos))
        x_pos = x_pos + BRICK_SEP + BRICK_WIDTH

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()
