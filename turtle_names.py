"""Contains a list of turtle names from a file"""


class TurtleNames:
    turtle_names = []

    @classmethod
    def __init__(cls):
        cls.reload_turtle_names()

    @classmethod
    def reload_turtle_names(cls):
        with open('turtle_names.txt') as f:
            TurtleNames.turtle_names = f.read().splitlines()
