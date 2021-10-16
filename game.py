# game.py
# main class
# authors: David, Erik

import pygame as py
from PYGAME_VARS import *
from time import time


class Game:
    def __init__(self, width=960, height=540, fps=30, ratio=(1920, 1080)):
        py.init()

        self.width, self.height = width, height
        self.fps = fps
        self._ratio = ratio # this should be treated as the original dimensions of the window
        self._scale = self.get_scale()


        self._screen = py.display.set_mode([self.width, self.height], py.RESIZABLE)
        self.screen = py.Surface((self.width, self.height))
        self.clock = py.time.Clock()

        #DEBUGGING average fps
        self.avr_fps = [self.fps for _ in range(50)]

    # gets scale of current window compared to original dimensions of the window
    def get_scale(self):
        scale = self.width / self._ratio[0]

        if self._ratio[1] * scale > self.height:
            scale = self.height / self._ratio[1]

            return scale

        return scale

    # blits main surface onto window
    def blit_screen(self):
        # determines position of main screen (for black borders)
        dx, dy = 0, 0

        if self._scale * self._ratio[0] < self.width:
            dx = int((self.width - self._scale * self._ratio[0]) / 2)
        elif self._scale * self._ratio[1] < self.height:
            dy = int((self.height - self._scale * self._ratio[1]) / 2)

        self._screen.blit(self.screen, (dx, dy))

    # main loop of the game
    def main(self):
        running = True
        start = time()

        while running:
            end = time()
            dt = end - start

            # event loop
            for event in py.event.get():
                # quit game
                if event.type == py.QUIT:
                    running = False
                    break
                self.event_handler(event)

            # updates physics
            self.physics_handler(dt)

            # updates screen
            self.render_handler(self._scale, dt)

            start = time()
            # sets fps
            self.clock.tick(self.fps)

    # handles complex user input
    def event_handler(self, event):
        #resize window event
        if event.type == py.VIDEORESIZE:
            self.width, self.height = event.w, event.h

            self._screen = py.display.set_mode((self.width, self.height), py.RESIZABLE)

            # resize actual window
            self._scale = self.get_scale()
            self.screen = py.transform.scale(self.screen, (int(self._ratio[0] * self._scale), int(self._ratio[1] * self._scale)))

    # handles physical processes
    # dt: time dif since the last main loop iteration
    def physics_handler(self, dt):
        pass

    # redraws the screen
    # scale: all rendered objects coordinates and dimensions must be scaled down with this factor before being blitted
    # onto the main surface
    # dt, DEBUGGING parameter: time dif since the last main loop iteration
    def render_handler(self, scale, dt):
        self._screen.fill(BLACK)
        self.screen.fill(DARK_GREY)

        # DEBUGGING: display fps
        if dt == 0:
            dt = 1

        self.avr_fps.pop(0)
        self.avr_fps.append(round(1 / dt, 2))
        self.screen.blit(standard_font.render(str(round(sum(self.avr_fps) / len(self.avr_fps))) + " fps", False, WHITE), (10, 10))

        self.blit_screen()
        py.display.update()
