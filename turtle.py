"""A model of a racing turtle"""

from random import randint

from turtle_names import TurtleNames


class Turtle:
    # turtle_names = TurtleNames()
    TurtleNames.__init__()

    def __init__(self):
        self.name = self.generate_name()
        self.speed = self.generate_speed()
        self.stamina = self.generate_stamina()

    def generate_name(self):
        turtle_name = TurtleNames.turtle_names[(
            randint(0, len(TurtleNames.turtle_names) - 1)
        )]
        TurtleNames.turtle_names.remove(turtle_name)

        return turtle_name

    def generate_speed(self):
        return randint(1, 10)

    def generate_stamina(self):
        return randint(1, 10)

    def regenerate_turtle_names(self):
        """This really shouldn't be here - it's just for the test method..."""
        TurtleNames.reload_turtle_names()
