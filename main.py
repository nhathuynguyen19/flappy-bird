import pygame, sys, math

import pygame.locals
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

# lop chim
class Bird:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        self.fall_speed = 0
        self.max_fall_speed = 10
        self.gravity = 0
        self.frames = []
        for i in range(1, 3):
            frame = pygame.image.load(f"img/bird/frame_{i}.png")
            frame = pygame.transform.scale(frame, (self.size, self.size))
            self.frames.append(frame)
        self.current_frame = 0
        self.frame_count = len(self.frames)
        self.frame_time = 100
        self.last_frame_update = pygame.time.get_ticks()
        self.angle = 0
        self.rotate_speed = 0
        self.rotate_begin = False
        self.shift_x = 0
        self.shift_y = 0

    def frame_update(self, current_time):
        if current_time - self.last_frame_update >= self.frame_time:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.last_frame_update = current_time

    def draw(self, screen):
        screen.blit(pygame.transform.rotate(bird.frames[bird.current_frame], bird.angle), (bird.x - bird.shift_x, bird.y - bird.shift_y))

    def fly(self):
        self.y += self.fall_speed
        if self.fall_speed < self.max_fall_speed:
            self.fall_speed += self.gravity
        if self.y >= window_height - window_height/4 - self.size + self.size / 9:
            self.y = window_height - window_height/4 - self.size + self.size / 9
            self.fall_speed = 0

    def rotate(self):
        if self.angle == 45:
            # distance to center
            distance_center_x = self.x + self.size / 2
            distance_center_y = self.y + self.size / 2
            # new x, y at near center
            x_new = self.x - distance_center_x
            y_new = self.y - distance_center_y + self.size
            # when rotate
            x_rotate = x_new * math.cos(self.angle) - y_new * math.sin(self.angle)
            y_rotate = y_new * math.sin(self.angle) + y_new * math.cos(self.angle)
            # distance to point origin
            self.shift_x = abs(x_rotate - x_new)
            self.shift_y = abs(y_rotate - y_new)
        if self.angle <= 45 and self.angle > -90 and self.rotate_begin == True:
            self.rotate_speed += 0.12
            self.angle -= self.rotate_speed
        if self.angle < -90:
            self.angle = -90
        if self.shift_x >= 0 and self.shift_y >=0:
            self.shift_x -= 0.2
            self.shift_y -= 0.2

# class cloud
class Cloud:
    def __init__(self, scale):
        self.img = pygame.image.load('img/cloud.png')
        self.img = pygame.transform.scale(self.img, (96 * scale, 66 * scale))

    def draw(self, screen, i, scale):
        if i % 192 == 0:
            screen.blit(self.img, (i, window_height - window_height / 4 - 66 * scale))

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
    bird.fly()
    bird.rotate()

    screen.fill(sky)
    screen.fill(brown, dirt)

    for i in range(0, 480):
        cloud.draw(screen, i, 2)
        line.draw(screen, i)
        tree_building.draw(screen, i, 2)

    bird.frame_update(current_time)
    bird.draw(screen)

    pygame.display.update()
    pygame.time.Clock().tick(60)