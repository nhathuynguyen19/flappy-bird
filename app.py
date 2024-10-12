import pygame, sys
from module.bird import Bird
from module.cloud import Cloud

pygame.init()

# cai icon game
app_icon = pygame.image.load('img/flappy_bird_icon.png')
pygame.display.set_icon(app_icon)

# name app
pygame.display.set_caption('Flappy Bird')

# tao do rong cua so
window_width = 320 + 160
window_height = 480 + 240
screen = pygame.display.set_mode((window_width, window_height))

# class line
class Line:
    def __init__(self, scale):
        # tao line
        self.line = pygame.image.load('img/line.png')
        self.line = pygame.transform.scale(self.line, (12 * scale, 11 * scale))
        self.speed = 0

    def draw(self, screen, i):
        if i % 24 == 0:
            self.speed += 0.1
            if self.speed >= 478:
                self.speed = 0
            i -= self.speed
            screen.blit(self.line, (i, window_height - window_height / 4))
            screen.blit(self.line, (i + 478, window_height - window_height / 4))

# class tree building
class Tree_Building:
    def __init__(self, scale):
        # tree
        self.img = pygame.image.load('img/tree_building.png')
        self.img = pygame.transform.scale(self.img, (48 * scale, 33 * scale))

    def draw(self, screen, i, scale):
        if i % 96 == 0:
            screen.blit(self.img, (i, window_height - window_height / 4 - 33 * scale))

# khai bao doi tuong bird
size_bird = 36
brown = (223, 215, 150)
sky = (113, 197, 207)
dirt = (0, window_height - window_height/4, window_width, window_height/4)
bird = Bird(size_bird, window_width / 2 - size_bird * 4, window_height / 2 - size_bird * 4)
line = Line(2)
tree_building = Tree_Building(2)
cloud = Cloud(2)
# vong lap chinh
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.fall_speed = -8
            bird.gravity = 0.5
            bird.angle = 45
            bird.rotate_begin = True
            bird.rotate_speed = 0

    current_time = pygame.time.get_ticks()
    bird.fly(window_height)
    bird.rotate()

    screen.fill(sky)
    screen.fill(brown, dirt)

    for i in range(0, 480):
        cloud.draw(screen, i, 2, window_height)
        line.draw(screen, i)
        tree_building.draw(screen, i, 2)

    bird.frame_update(current_time)
    bird.draw(screen)

    pygame.display.update()
    pygame.time.Clock().tick(60)
