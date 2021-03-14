import random as rnd
import pygame


class Fuel:
    def __init__(self, screensize):
        self.pos = [screensize[0], rnd.randint(0, screensize[1])]
        self.vel = [rnd.randint(1, 10) * -1, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def render(self, window):
        pygame.draw.rect(window, (255, 255, 0), self.rect)