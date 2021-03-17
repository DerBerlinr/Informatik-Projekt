import random as rnd
import pygame


class Fuel:
    def __init__(self, screensize):
        self.pos = [screensize[0], rnd.randint(0, screensize[1])]
        self.vel = [rnd.randint(1, 10) * -1, 0]
        self.fuelImg = pygame.image.load('plus.png')
        self.fuelImg = pygame.transform.scale(self.fuelImg, (50, 50))
        self.rect = self.fuelImg.get_rect(topleft=(self.pos[0], self.pos[1]))

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = self.fuelImg.get_rect(topleft=(self.pos[0], self.pos[1]))

    def render(self, window):
        window.blit(self.fuelImg, self.rect)