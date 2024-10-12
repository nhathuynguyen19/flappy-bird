import pygame, math

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
        screen.blit(pygame.transform.rotate(self.frames[self.current_frame], self.angle), (self.x - self.shift_x, self.y - self.shift_y))

    def fly(self, window_height):
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