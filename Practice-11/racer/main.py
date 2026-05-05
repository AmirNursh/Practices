import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_x = 180
player_y = 500

enemy_x = random.randint(50, 350)
enemy_y = -100
enemy_speed = 5

coins = []
coin_count = 0


# Generate coins with different weights
def create_coin():
    return {
        "x": random.randint(50, 350),
        "y": random.randint(-500, -50),
        "weight": random.choice([1, 2, 3])
    }


for _ in range(3):
    coins.append(create_coin())

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 40, 60))

    # Enemy
    enemy_y += enemy_speed
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 40, 60))

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, 350)

    # Coins
    for coin in coins:
        coin["y"] += 5

        pygame.draw.circle(
            screen,
            (255, 215, 0),
            (coin["x"], coin["y"]),
            15
        )

        # Collision with player
        if abs(player_x - coin["x"]) < 30 and abs(player_y - coin["y"]) < 30:
            coin_count += coin["weight"]
            coin.update(create_coin())

        if coin["y"] > HEIGHT:
            coin.update(create_coin())

    # Increase enemy speed every 5 coins
    if coin_count % 5 == 0 and coin_count != 0:
        enemy_speed = 5 + coin_count // 5

    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Coins: {coin_count}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()