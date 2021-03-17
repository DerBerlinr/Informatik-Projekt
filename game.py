import pygame
from pygame.locals import *
from asteroid import Asteroid
import random
from fuel import Fuel
from checkpoint import Checkpoint
from bullet import Bullet
import ctypes


class Game:
    def __init__(self, cars):
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)

        self.screen_size = self.screen_width, self.screen_height = 1000, 800
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Space Race')
        self.background = pygame.image.load("space.webp")
        self.background = pygame.transform.scale(self.background, (1000, 800))

        self.clock = pygame.time.Clock()
        self.fps_limit = 60
        self.running = True

        self.cars = []
        for car in cars:
            self.cars.append([car, 0])
        self.asteroids = []
        self.fuel_bubbles = []
        self.checkpoints = []
        self.bullets = []
        self.last_checkpoint = []  # [Score, Fuel]
        self.checkpoint_counter = 1

        self.score = 0

    def run(self):
        while self.running:
            self.clock.tick(self.fps_limit)
            self.score += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # SPAWNING OBJECTS -----------------------------------------------------------------------------------------
            level = 1
            if self.score > 500:
                level = 2
            if self.score > 1000:
                level = 3
            if self.score > 1250:
                level = 4
            if random.randint(1, int(30 / level)) == 1:
                if random.randint(1, 15) == 1:
                    new_fuel_bubble = Fuel(self.screen_size)
                    self.fuel_bubbles.append(new_fuel_bubble)
                else:
                    new_asteroid = Asteroid(self.screen_size, self.score / 10000 + 1)
                    self.asteroids.append(new_asteroid)
            if random.randint(1, 1000) == 1:
                new_checkpoint = Checkpoint(self.screen_size, self.checkpoint_counter)
                self.checkpoints.append(new_checkpoint)
                self.checkpoint_counter += 1

            # INPUTS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            keys = pygame.key.get_pressed()
            # MOVEMENT -------------------------------------------------------------------------------------------------
            if self.cars[0][0].fuel >= 5:
                if keys[K_LEFT]:
                    self.cars[0][0].vel[0] -= 0.1
                    self.cars[0][0].fuel -= 5
                if keys[K_RIGHT]:
                    self.cars[0][0].vel[0] += 0.1
                    self.cars[0][0].fuel -= 5
                if keys[K_UP]:
                    self.cars[0][0].vel[1] -= 0.1
                    self.cars[0][0].fuel -= 5
                if keys[K_DOWN]:
                    self.cars[0][0].vel[1] += 0.1
                    self.cars[0][0].fuel -= 5
            if self.cars[0][0].fuel < 1000:
                self.cars[0][0].fuel += 1
            # BULLET ---------------------------------------------------------------------------------------------------
            if keys[K_SPACE]:
                if self.cars[0][0].fuel >= 20:
                    new_bullet = Bullet(self.cars[0][0].pos)
                    self.bullets.append(new_bullet)
                    self.cars[0][0].fuel -= 20

            # "KI" INPUTS ----------------------------------------------------------------------------------------------
            # because real ki not working (i tried hard)
            for car in self.cars:
                if car != self.cars[0]:
                    if random.randint(1, 10) == 1:
                        if random.randint(1, 4) == 1:
                            if car[0].pos[0] < (self.screen_width - 50) and car[0].pos[1] < (self.screen_height - 50):
                                car[0].vel[0] += random.random()
                                car[0].vel[1] += random.random()
                            else:
                                car[0].vel[0] -= random.random()
                                car[0].vel[1] -= random.random()
                        if random.randint(1, 4) == 2:
                            if car[0].pos[0] > 50 and car[0].pos[1] < (self.screen_height - 50):
                                car[0].vel[0] -= random.random()
                                car[0].vel[1] += random.random()
                            else:
                                car[0].vel[0] += random.random()
                                car[0].vel[1] -= random.random()
                        if random.randint(1, 4) == 3:
                            if car[0].pos[0] < (self.screen_width - 50) and car[0].pos[1] > 50:
                                car[0].vel[0] += random.random()
                                car[0].vel[1] -= random.random()
                            else:
                                car[0].vel[0] -= random.random()
                                car[0].vel[1] += random.random()
                        if random.randint(1, 4) == 4:
                            if car[0].pos[0] > 50 and car[0].pos[1] > 50:
                                car[0].vel[0] -= random.random()
                                car[0].vel[1] -= random.random()
                            else:
                                car[0].vel[0] += random.random()
                                car[0].vel[1] += random.random()




            # Collision detection -------------------------------------------------------------------------------------------------------------------------------------------------------------
            for car in self.cars:
                asteroid_rectlist = []
                fuelbubble_rectlist = []
                checkpoint_rectlist = []
                bullet_rectlist = []
                for asteroid in self.asteroids:
                    asteroid_rectlist.append(asteroid.rect)
                for fuelbubble in self.fuel_bubbles:
                    fuelbubble_rectlist.append(fuelbubble.rect)
                for checkpoint in self.checkpoints:
                    checkpoint_rectlist.append(checkpoint.rect)
                for bullet in self.bullets:
                    bullet_rectlist.append(bullet.rect)
                old_pos_car, new_pos_car = car[0].new_pos()

                # WALLS ------------------------------------------------------------------------------------------------
                if new_pos_car[0] > 0 and new_pos_car[0] < self.screen_width - 50 and new_pos_car[1] > 0 and new_pos_car[1] < self.screen_height - 50:
                    # ASTEROIDS ----------------------------------------------------------------------------------------
                    cl = car[0].rect.collidelist(asteroid_rectlist)
                    if cl != -1:
                        # Type 2
                        if self.asteroids[cl].type != 1:
                            if car == self.cars[0]:
                                self.running = False
                            else:
                                self.cars.remove(car)
                        else:
                            # Type 1
                            if car[0].fuel > 200:
                                car[0].fuel -= 200
                                self.asteroids.pop(cl)
                            else:
                                if car == self.cars[0]:
                                    self.running = False
                                else:
                                    self.cars.remove(car)
                    # FUEL ---------------------------------------------------------------------------------------------
                    cl_f = car[0].rect.collidelist(fuelbubble_rectlist)
                    if cl_f != -1:
                        car[0].fuel += 500
                        self.fuel_bubbles.pop(cl_f)
                    # CHECKPOINTS --------------------------------------------------------------------------------------
                    cl_c = car[0].rect.collidelist(checkpoint_rectlist)
                    if cl_c != -1:
                        if not(self.checkpoints[cl_c].nr in car[0].passed_checkpoints):
                            car[1] += (5 - self.checkpoints[cl_c].passed)
                            self.checkpoints[cl_c].passed += 1
                            car[0].passed_checkpoints.append(self.checkpoints[cl_c].nr)
                else:
                    if car == self.cars[0]:
                        self.running = False
                    else:
                        self.cars.remove(car)

                # BULLETS ----------------------------------------------------------------------------------------------
                asteroid_rectlist = []
                for asteroid in self.asteroids:
                    asteroid_rectlist.append(asteroid.rect)
                for bullet in self.bullets:
                    cl_b = bullet.rect.collidelist(asteroid_rectlist)
                    if cl_b != -1:
                        self.asteroids.pop(cl_b)
                        self.bullets.remove(bullet)
                    else:
                        if bullet.pos[0] < self.screen_width:
                            bullet.new_pos()
                        else:
                            self.bullets.remove(bullet)



            # DEL ASTEROIDS IF OUT OF SIGHT ----------------------------------------------------------------------------
            for asteroid in self.asteroids:
                if asteroid.pos[0] > 0:
                    asteroid.new_pos()
                else:
                    self.asteroids.remove(asteroid)

            # DEL FUEL IF OUT OF SIGHT ---------------------------------------------------------------------------------
            for fuel in self.fuel_bubbles:
                if fuel.pos[0] > 0:
                    fuel.new_pos()
                else:
                    self.fuel_bubbles.remove(fuel)

            # DEL CHECKPOINTS IF OUT OF SIGHT --------------------------------------------------------------------------
            for checkpoint in self.checkpoints:
                if checkpoint.pos[0] > 0:
                    checkpoint.new_pos()
                else:
                    self.checkpoints.remove(checkpoint)

            # RENDERING -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self.screen.blit(self.background, (0, 0))
            for car in self.cars:
                car[0].render(self.screen)
            for asteroid in self.asteroids:
                asteroid.render(self.screen)
            for fuel in self.fuel_bubbles:
                fuel.render(self.screen)
            for checkpoint in self.checkpoints:
                checkpoint.render(self.screen)
            for bullet in self.bullets:
                bullet.render(self.screen)
            # Fuel bar
            pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(5, self.screen_height - 15, self.cars[0][0].fuel / 2, 10))
            pygame.draw.rect(self.screen, (128, 128, 128), pygame.Rect(5, self.screen_height - 15, 500, 10), 1)

            pygame.display.flip()
        if ctypes.windll.user32.MessageBoxW(0, "You crashed into something \nYour Score: "+str(self.score)+"\nYour Points: "+str(self.cars[0][1]), "You Lost :(", 5) == 4:
            self.asteroids = []
            self.fuel_bubbles = []
            self.bullets = []
            self.checkpoints = []
            self.score = 0
            for car in self.cars:
                car[1] = 0
                car[0].pos = [300, 200]
                car[0].vel = [0, 0]
                car[0].fuel = 1000
            self.running = True
            self.run()