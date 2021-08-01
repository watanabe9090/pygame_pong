import pygame
import sys
from variables import *
from Player import *
from Enemy import *
from Ball import *
from Score import *

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 32)
        self.running = False
        pygame.display.set_caption('ぽン')

    def start(self):
        self.running = True
        self.player = Player(self.screen)
        self.enemy = Enemy(self.screen)
        self.ball = Ball(self.screen)
        self.player_score = Score(self.screen, self.font, SCREEN_WIDTH/2-30, SCREEN_HEIGHT/4)
        self.enemy_score = Score(self.screen, self.font, SCREEN_WIDTH/2+12, SCREEN_HEIGHT/4)

    def draw(self):
        self.screen.fill((0, 0, 0));
        pygame.draw.aaline(self.screen,
            (255,255,255),
            (SCREEN_WIDTH/2,0),
            (SCREEN_WIDTH/2, SCREEN_HEIGHT))

        # Entities draw
        self.player.draw()
        self.enemy.draw()
        self.ball.draw()
        self.player_score.draw()
        self.enemy_score.draw()


    def update(self):
        self.player.update()
        self.enemy.update(self.ball.y+self.ball.side/2)
        self.ball.update()
        # Player Point
        if(self.ball.x > SCREEN_WIDTH-self.ball.side):
            print("Point from Player")
            self.player_score.increment()
            self.ball.reset()
        # Enemy Point
        if(self.ball.x < 0):
            print("Point from Enemy")
            self.enemy_score.increment()
            self.ball.reset()
        
        if self.ball.shape.colliderect(self.player.shape) and self.ball.speed_x < 0:
            self.ball.speed_x *= -1
            self.ball.increase_speed()
        if self.ball.shape.colliderect(self.enemy.shape) and self.ball.speed_x > 0:
            self.ball.speed_x *= -1
            self.ball.increase_speed()
        # Scores
        if(self.player_score.score >= MAX):
            pygame.quit()
            sys.exit()
        if(self.enemy_score.score >= MAX):
            pygame.quit()
            sys.exit()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player.moving_down = True
                    elif event.key == pygame.K_UP:
                        self.player.moving_up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player.moving_down = False
                    elif event.key == pygame.K_UP:
                        self.player.moving_up = False

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(TICK)

game = Game();
game.start();
game.run();
