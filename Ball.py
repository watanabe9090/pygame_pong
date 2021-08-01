import pygame;
import math;
import random;
from variables import *;
class Ball:
    def __init__(self, screen):
        self.side = 30;
        self.x = (SCREEN_WIDTH/2 - self.side/2);
        self.y = (SCREEN_HEIGHT/2 - self.side/2);
        self.shape = pygame.Rect(self.x, self.y, self.side, self.side);
        self.color = (255, 255, 255);
        self.screen = screen;
        self.speed_x = 7 * random.choice([-1,1]);
        self.speed_y = 7 * random.choice([-1,1]);
        self.timer = 60

    def increase_speed(self):
        self.speed_x *= 1.05;
        self.speed_y *= 1.02;

    def reset(self):
        self.x = (SCREEN_WIDTH/2 - self.side/2);
        self.y = (SCREEN_HEIGHT/2 - self.side/2);
        self.speed_x = 7 * random.choice([-1,1]);
        self.speed_y = 7 * random.choice([-1,1]);
        self.shape.x = self.x;
        self.shape.y = self.y;
        self.timer = 60

    def update(self):
        if(self.timer <= 0):
            self.x += self.speed_x;
            self.y += self.speed_y;
            if (self.y+self.side >= SCREEN_HEIGHT) or (self.y) < 0:
                self.speed_y *= -1;
            self.shape.x = self.x;
            self.shape.y = self.y;
        else:
            self.timer -=1
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape);
