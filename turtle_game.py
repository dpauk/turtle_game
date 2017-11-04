"""A turtle racing game"""

import sys

from race import Race
# from turtle import Turtle


def main():
    """The main entry point for the turtle game"""
    race = Race()
    print("Race name: {}".format(race.name))
    print("Race length: {} metres".format(race.length))
    print("Number of competitors: {}".format(race.number_of_competitors))


if __name__ == '__main__':
    sys.exit(main())
