import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

pygame.init()


def game_over(main_surface):
    """
    This function shows a "game over" screen and plays a "whoosh" sound
    :param main_surface:
    :return: none
    """
    main_surface.fill((0, 0, 0))
    my_font = pygame.font.SysFont("Helvetica", 60)
    label = my_font.render("GAME OVER", 1, (0, 255, 255))
    main_surface.blit(label, (85, 250))
    sound = pygame.mixer.Sound('fly.wav')
    sound.play()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


def win(main_surface):
    """
    This function shows a "win" screen and plays a "cheer" sound
    :param main_surface:
    :return: none
    """
    main_surface.fill((0, 0, 0))
    my_font = pygame.font.SysFont("Helvetica", 60)
    label = my_font.render("YOU WIN", 1, (0, 255, 255))
    main_surface.blit(label, (85, 250))
    sound = pygame.mixer.Sound('cheer.wav')
    sound.play()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


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

    # Sets up the colors
    MAGENTA = (255, 0, 255)
    PURPLE = (75, 0, 130)
    BLUE = (25, 25, 140)
    YELLOW =(0, 250, 154)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    colors = [MAGENTA, PURPLE, BLUE, CYAN, YELLOW]

    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    bg = pygame.image.load("stars.png")
    main_surface.blit(bg, (0, 0))
    # main_surface.fill((0, 0, 0))

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
    for color in colors:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
                my_brick.rect.x = x_pos
                my_brick.rect.y = y_pos
                bricks_group.add(my_brick)
                main_surface.blit(my_brick.image, (x_pos, y_pos))
                x_pos = x_pos + BRICK_SEP + BRICK_WIDTH
            y_pos += BRICK_SEP + BRICK_HEIGHT
            x_pos = BRICK_SEP

    # this ads the paddle to the bottom of the screen
    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_group.add(my_paddle)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)

    # this adds the ball to the screen
    my_ball = ball.Ball(WHITE, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2
    main_surface.blit(my_ball.image, my_ball.rect)
    tries = 0

    while True:
        # this adds the galaxy background to the main screen
        main_surface.fill(BLACK)
        main_surface.blit(bg, (0, 0))
        # this adds all the bricks to the main screen
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        # this adds the paddle to the main screen and makes its x coordinates move with the x coordinates of the mouse
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        main_surface.blit(my_ball.image, my_ball.rect)
        my_ball.move()
        my_ball.collide(paddle_group)
        my_ball.collide_brick(bricks_group)
        #  this if statement repositions the ball to the middle fo the screen if it hits the bottom of the screen
        #  and it adds 1 to your number of tries
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            tries += 1
            my_ball.rect.y = APPLICATION_HEIGHT / 2
        #  this if statement ends the game if your number of tries is greater than or equal to 3
        # it says greater than or equal to three because if it just equals three the ball would keep hitting the bottom
        # of the screen over and over again then the game would never end
        if tries >= 3:
            game_over(main_surface)
        # if you get rid of all the bricks this will say you won the game
        if len(bricks_group) == 0:
            win(main_surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
