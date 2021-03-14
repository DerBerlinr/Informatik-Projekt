import pygame


class Car:
    def __init__(self):
        self.pos = [300, 200]
        self.vel = [0, 0]
        self.carImg = pygame.image.load('spaceship.png')
        self.carImg = pygame.transform.scale(self.carImg, (50, 50))
        self.rect = self.carImg.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.fuel = 100

    def render(self, window):
        window.blit(self.carImg, self.rect)


    def new_pos(self):
        old = self.pos[:]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect = self.carImg.get_rect(topleft=(self.pos[0], self.pos[1]))
        return old, self.pos


    def set_pos(self, pos):
        self.pos = pos
        return self.pos


