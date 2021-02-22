class Car:
    def __init__(self):
        self.pos = (0, 0)
        self.vel = (0, 0)

    def accelerate(self, dir):
        # dir: 1 -> up 2->DOWN 3->left 4->right
        if dir == 1:
            vel += (0, 0.1)
        elif dir == 2:
            vel -= (0, -0.1)
        elif dir == 3:
            vel += (0.1, 0)
        elif dir == 4:
            vel -= (-0.1, 0)

    def new_pos(self):
        self.pos += self.vel
        return self.pos
