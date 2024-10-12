import pygame

# class cloud
class Cloud:
    def __init__(self, scale):
        self.img = pygame.image.load('img/cloud.png')
        self.img = pygame.transform.scale(self.img, (96 * scale, 66 * scale))

    def draw(self, screen, i, scale, window_height):
        if i % 192 == 0:
            screen.blit(self.img, (i, window_height - window_height / 4 - 66 * scale))