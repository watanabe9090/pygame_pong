import pygame
from variables import *

class Score():
  def __init__(self, screen, font, x, y):
    self.screen = screen
    self.font = font
    self.x = x
    self.y = y
    self.score = 0
    self.max = MAX

  def increment(self):
    self.score += 1

  def draw(self):
    text = self.font.render(f"{self.score}", False, (255,255,255))
    self.screen.blit(text, (self.x, self.y) )