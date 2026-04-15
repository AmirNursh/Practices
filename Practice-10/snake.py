import pygame
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]
dx, dy = CELL, 0

food = (random.randrange(0, WIDTH, CELL),
        random.randrange(0, HEIGHT, CELL))

score = 0
level = 1
speed = 7

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = CELL, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, CELL

    head = (snake[0][0] + dx, snake[0][1] + dy)

    # Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("Game Over")
        break

    # Self collision
    if head in snake:
        print("Game Over")
        break

    snake.insert(0, head)

    # Food collision
    if head == food:
        score += 1

        # Level system
        if score % 4 == 0:
            level += 1
            speed += 2

        # Generate food not on snake
        while True:
            food = (
                random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL)
            )
            if food not in snake:
                break
    else:
        snake.pop()

    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
