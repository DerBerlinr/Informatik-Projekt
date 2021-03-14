from game import *
from car import *

if __name__ == '__main__':
    cars = []
    for i in range(int(input("Wie viele Autos? -> "))):
        temp_car = Car()
        cars.append(temp_car)

    game = Game(cars)

    game.run()
