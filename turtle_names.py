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

    @classmethod
    def get_length_turtle_names(cls):
        return len(TurtleNames.turtle_names)

    @classmethod
    def get_turtle_name(cls, position):
        return TurtleNames.turtle_names[position]

    @classmethod
    def remove_turtle_name(cls, turtle_name):
        TurtleNames.turtle_names.remove(turtle_name)
