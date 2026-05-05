import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

shape = "square"
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "square"

            elif event.key == pygame.K_2:
                shape = "right_triangle"

            elif event.key == pygame.K_3:
                shape = "equilateral_triangle"

            elif event.key == pygame.K_4:
                shape = "rhombus"

    # Draw square
    if shape == "square":
        pygame.draw.rect(screen, (0, 0, 255), (300, 200, 200, 200))

    # Draw right triangle
    elif shape == "right_triangle":
        pygame.draw.polygon(
            screen,
            (255, 0, 0),
            [(300, 400), (300, 200), (500, 400)]
        )

    # Draw equilateral triangle
    elif shape == "equilateral_triangle":
        pygame.draw.polygon(
            screen,
            (0, 255, 0),
            [(400, 150), (300, 350), (500, 350)]
        )

    # Draw rhombus
    elif shape == "rhombus":
        pygame.draw.polygon(
            screen,
            (255, 165, 0),
            [(400, 150), (500, 300), (400, 450), (300, 300)]
        )

    pygame.display.update()

pygame.quit()