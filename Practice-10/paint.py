import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)

color = BLACK
mode = "draw"
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = BLUE
            elif event.key == pygame.K_3:
                color = GREEN

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            if mode == "rectangle":
                rect = pygame.Rect(
                    start_pos[0],
                    start_pos[1],
                    end_pos[0] - start_pos[0],
                    end_pos[1] - start_pos[1]
                )
                pygame.draw.rect(screen, color, rect, 2)

            elif mode == "circle":
                radius = int(
                    ((end_pos[0] - start_pos[0]) ** 2 +
                     (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                )
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        # Drawing
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if mode == "draw":
                    pygame.draw.circle(screen, color, event.pos, 4)
                elif mode == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, 10)

    pygame.display.update()

pygame.quit()