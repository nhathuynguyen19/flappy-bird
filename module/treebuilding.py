import pygame

# class tree building
class Tree_Building:
    def __init__(self, scale):
        # tree
        self.img = pygame.image.load('img/tree_building.png')
        self.img = pygame.transform.scale(self.img, (48 * scale, 33 * scale))

    def draw(self, screen, i, scale, window_height):
        if i % 96 == 0:
            screen.blit(self.img, (i, window_height - window_height / 4 - 33 * scale))