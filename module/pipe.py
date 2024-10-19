import pygame
class Pipe:
    def __init__(self):
        scale = 0.5
        self.image = pygame.image.load("img/pipe.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

    def draw(self, screen, window_width, window_height):
        screen.blit(self.image, (0, (window_height / 4) * 3 / 2 + 32))

        self.image = pygame.transform.flip(self.image)
        self.image = pygame.transform.rotate(self.image, (180))
        screen.blit(self.image, (0, (window_height / 4) * 3 / 2 + 32))