import random as rnd
import pygame
import copy


class Bullet:
    def __init__(self, pos):
        self.pos = copy.deepcopy(pos)
        self.vel = [4, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 5, 10)

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 5, 10)

    def render(self, window):
        pygame.draw.rect(window, (255, 0, 255), self.rect)
