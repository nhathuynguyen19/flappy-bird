import pygame, random
class Pipe:
    def __init__(self, x, y):
        scale = 0.5
        self.x = 480
        self.y = y
        self.random_y = 0
        self.image = pygame.image.load("img/pipe.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

    def randomX(self):
        self.random_y = random.randint(-150, 150)

    def drawPipeBottom(self, screen):
        screen.blit(self.image, (self.x, self.random_y + self.y - (self.y / 4) - 215))

    def drawPipeTop(self, screen):
        self.image = pygame.transform.flip(self.image, False, True)
        screen.blit(self.image, (self.x, -372 + 215 + self.random_y))
        self.image = pygame.transform.flip(self.image, False, True)
        
    def dropX(self):
        self.x -= 2
        if (self.x <= -62):
            self.x = 480
