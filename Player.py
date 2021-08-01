import pygame;
from variables import *;

class Player:
    def __init__(self, screen):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = SCREEN_WIDTH/20
        self.y = SCREEN_HEIGHT/2
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 255)
        self.screen = screen
        self.speed_y = 5
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if (self.moving_up):
            self.y -= self.speed_y
        if (self.moving_down):
            self.y += self.speed_y
        #Collisions
        if (self.y+self.height >= SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT-self.height
        elif (self.y) < 0:
            self.y = 0
        self.shape.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)
