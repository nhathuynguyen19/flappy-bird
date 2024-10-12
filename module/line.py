import pygame

# class line
class Line:
    def __init__(self, scale):
        # tao line
        self.line = pygame.image.load('img/line.png')
        self.line = pygame.transform.scale(self.line, (12 * scale, 11 * scale))
        self.speed = 0

    def draw(self, screen, i, window_height):
        if i % 24 == 0:
            self.speed += 0.1
            if self.speed >= 478:
                self.speed = 0
            i -= self.speed
            screen.blit(self.line, (i, window_height - window_height / 4))
            screen.blit(self.line, (i + 478, window_height - window_height / 4))