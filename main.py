from game import *
from car import *
import time

if __name__ == '__main__':
    cars = []
    for i in range(int(input("Wie viele Autos? -> "))):
        temp_car = Car()
        cars.append(temp_car)

    game = Game(cars)
    time.sleep(1)
    game.run()
