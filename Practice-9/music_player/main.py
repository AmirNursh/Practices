import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 200))
font = pygame.font.SysFont(None, 36)

player = MusicPlayer()

running = True

while running:
    screen.fill((255, 255, 255))

    text = font.render(
        f"Track: {player.current + 1}",
        True,
        (0, 0, 0)
    )

    screen.blit(text, (200, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.previous()

            elif event.key == pygame.K_q:
                running = False

    pygame.display.update()

pygame.quit()