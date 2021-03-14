import random as rnd
import pygame


class Asteroid:
    def __init__(self, screensize, speed):
        self.pos = [screensize[0], rnd.randint(0, screensize[1])]
        self.vel = [rnd.randint(1, 10) * -1 * speed, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)
        self.type = rnd.randint(1, 2)

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def render(self, window):
        if self.type == 1:
            pygame.draw.rect(window, (0, 0, 255), self.rect)
        else:
            pygame.draw.rect(window, (255, 0, 0), self.rect)
