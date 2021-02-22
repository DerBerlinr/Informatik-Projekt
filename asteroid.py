import random as rnd


class Asteroid:
    def __init__(self, screensize):
        self.pos = (screensize[1], rnd.randint(screensize[2]))
        self.vel = (rnd.randint(0, -10), rnd.randint(-10, 10))

    def new_pos(self):
        self.pos += self.vel
        return self.pos
