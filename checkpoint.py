import random as rnd
import pygame


class Checkpoint():
    def __init__(self, screensize, nr):
        self.nr = nr
        self.screensize = screensize
        self.pos = [screensize[0], 0]
        self.vel = [-5, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, screensize[1])
        self.passed = 0

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, self.screensize[1])

    def render(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)