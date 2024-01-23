"""
A simple arkanoid game made with pygame
As you break more blocks, the ball moves faster
by. R1NM
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")


# Define the paddle
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (width - self.width) // 2
        self.y = height - 50
        self.speed = 5

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < width - self.width:
            self.x += self.speed

    def make_object(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


# Define the ball
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = width // 2
        self.y = height // 2
        self.dx = random.choice([-2, 2])
        self.dy = -2

    def move(self):
        ball.x += ball.dx
        ball.y += ball.dy

    def wall(self):
        if ball.x <= 0 or ball.x >= width:
            ball.dx *= -1
        if ball.y <= 0:
            ball.dy *= -1

    def check_gameover(self):
        if ball.y >= height:
            print("OH! YOU LOSE!")
            return False
        return True

    def make_object(self):
        return pygame.Rect(self.x, self.y, self.radius, self.radius)


# Define bricks
brick_width = 70
brick_height = 20
brick_rows = 5
brick_cols = width // brick_width

# add bricks
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + 1) + 10
        brick_y = row * (brick_height + 1) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Game loop
running = True
clock = pygame.time.Clock()

paddle = Paddle()
ball = Ball()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right()

    # Move the ball
    ball.move()

    # Ball collisions with walls
    ball.wall()

    ball_obj = ball.make_object()
    paddle_obj = paddle.make_object()

    # Ball collision with paddle
    if ball_obj.colliderect(paddle_obj):
        ball.dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball_obj.colliderect(brick):
            bricks.remove(brick)
            ball.dy *= -1
            # Speed up the ball
            ball.dy *= 1.02
            ball.dx *= 1.02
            break

    # Game over if ball goes below the paddle
    running = ball.check_gameover()

    # Game end if all the bricks are gone
    if len(bricks) == 0:
        running = False
        clock.tick(60)
        print("GOOD! YOU WIN!")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), [paddle.x, paddle.y, paddle.width, paddle.height])

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), [ball.x, ball.y], ball.radius)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, (255, 255, 255), brick)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
