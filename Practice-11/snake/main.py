import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100)]
dx = 20
dy = 0


# Generate food with weight
def create_food():
    return {
        "x": random.randrange(0, WIDTH, 20),
        "y": random.randrange(0, HEIGHT, 20),
        "weight": random.choice([1, 2, 3]),
        "spawn_time": time.time()
    }


food = create_food()
score = 0

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dx = -20
        dy = 0

    if keys[pygame.K_RIGHT]:
        dx = 20
        dy = 0

    if keys[pygame.K_UP]:
        dx = 0
        dy = -20

    if keys[pygame.K_DOWN]:
        dx = 0
        dy = 20

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # Food disappears after 5 seconds
    if time.time() - food["spawn_time"] > 5:
        food = create_food()

    if head == (food["x"], food["y"]):
        score += food["weight"]

        # Grow depending on food weight
        for _ in range(food["weight"]):
            snake.append(snake[-1])

        food = create_food()
    else:
        snake.pop()

    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*part, 20, 20))

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (food["x"], food["y"], 20, 20)
    )

    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(10)

pygame.quit()