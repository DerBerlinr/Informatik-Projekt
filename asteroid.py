import random as rnd
import pygame


class Asteroid:
    def __init__(self, screensize, speed):
        self.pos = [screensize[0], rnd.randint(0, screensize[1])]
        self.vel = [rnd.randint(1, 10) * -1 * speed, 0]
        self.astImg = pygame.image.load('asteroid.jpg')
        self.ast2Img = pygame.image.load('asteroid2.png')
        self.astImg = pygame.transform.scale(self.astImg, (50, 50))
        self.ast2Img = pygame.transform.scale(self.ast2Img, (50, 50))
        self.rect = self.astImg.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.type = rnd.randint(1, 2)

    def new_pos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = self.astImg.get_rect(topleft=(self.pos[0], self.pos[1]))

    def render(self, window):
        if self.type == 1:
            window.blit(self.astImg, self.rect)
        else:
            window.blit(self.ast2Img, self.rect)
