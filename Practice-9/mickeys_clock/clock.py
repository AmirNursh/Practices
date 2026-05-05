import pygame
import datetime


class MickeyClock:
    def __init__(self):
        self.clock_img = pygame.image.load("images/mickeyclock.jpeg")

    def draw(self, screen):
        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        minute_angle = -(minutes * 6)
        second_angle = -(seconds * 6)

        rotated_minute = pygame.transform.rotate(
            self.right_hand, minute_angle
        )
        rotated_second = pygame.transform.rotate(
            self.left_hand, second_angle
        )

        screen.blit(self.clock_img, (0, 0))

        minute_rect = rotated_minute.get_rect(center=(250, 250))
        second_rect = rotated_second.get_rect(center=(250, 250))

        screen.blit(rotated_minute, minute_rect)
        screen.blit(rotated_second, second_rect)