import pygame
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# Load image
bg = pygame.image.load("images/mickeyclock.jpeg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


def draw_hand(angle, length, color, width):
    x = CENTER[0] + length * math.cos(math.radians(angle - 90))
    y = CENTER[1] + length * math.sin(math.radians(angle - 90))

    pygame.draw.line(
        screen,
        color,
        CENTER,
        (x, y),
        width
    )


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    minute_angle = minutes * 6
    second_angle = seconds * 6

    screen.blit(bg, (0, 0))

    # Right hand = minutes
    draw_hand(minute_angle, 180, (0, 0, 255), 8)

    # Left hand = seconds
    draw_hand(second_angle, 220, (255, 0, 0), 4)

    pygame.display.update()
    clock.tick(1)

pygame.quit()