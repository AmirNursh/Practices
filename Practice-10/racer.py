import pygame
import random

# Initialize pygame and font module
pygame.init()
pygame.font.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (80, 80, 80)

# Player car
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 7

# Enemy car
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

# Coins
coins = []
coin_count = 0

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 40:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 50)

    # Random coin spawn
    if random.randint(1, 100) == 1:
        coins.append([random.randint(20, WIDTH - 20), 0])

    # Coin movement and collision
    for coin in coins[:]:
        coin[1] += 4

        if abs(player_x - coin[0]) < 30 and abs(player_y - coin[1]) < 30:
            coin_count += 1
            coins.remove(coin)
        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Collision with enemy
    if abs(player_x - enemy_x) < 40 and abs(player_y - enemy_y) < 60:
        print("Game Over")
        running = False

    # Draw objects
    pygame.draw.rect(screen, RED, (player_x, player_y, 40, 60))
    pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y, 40, 60))

    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin, 10)

    # Coin counter
    text = font.render(f"Coins: {coin_count}", True, WHITE)
    screen.blit(text, (WIDTH - 150, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()