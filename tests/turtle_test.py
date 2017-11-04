"""The test scripts for the turtle class"""

from turtle import Turtle


def test_generate_name_generates_valid_name():
    with open('turtle_names.txt') as f:
        turtle_names = f.read().splitlines()

    assert Turtle().generate_name() in turtle_names


def test_generate_name_never_generates_same_turtle_twice():
    """Generates 20 sets of 5 turtles to ensure that none contain the same
    turtle twice"""
    for i in range(0, 20):
        turtles = []
        Turtle().regenerate_turtle_names()
        for j in range(0, 5):
            turtles.append(Turtle().name)
        duplicates = [x for n, x in enumerate(turtles)
                      if x in turtles[:n]]
        assert len(duplicates) == 0


def test_generate_speed_generates_valid_number():
    """Generates 20 numbers to try and ensure that all numbers are valid"""
    for i in range(0, 20):
        Turtle().regenerate_turtle_names()
        generated_speed = Turtle().generate_speed()
        assert generated_speed >= 1
        assert generated_speed <= 10


def test_generate_stamina_generates_valid_number():
    """Generates 20 numbers to try and ensure that all numbers are valid"""
    for i in range(0, 20):
        Turtle().regenerate_turtle_names()
        generated_stamina = Turtle().generate_stamina()
        assert generated_stamina >= 1
        assert generated_stamina <= 10
