"""A model of a racing turtle"""

from random import randint


class Turtle:
    def __init__(self):
        self.name = self.generate_name()
        self.speed = self.generate_speed()
        self.stamina = self.generate_stamina()

    def generate_name(self):
        with open('turtle_names.txt') as f:
            turtle_names = f.read().splitlines()

        return turtle_names[randint(0, len(turtle_names) - 1)]

    def generate_speed(self):
        return randint(1, 10)

    def generate_stamina(self):
        return randint(1, 10)
