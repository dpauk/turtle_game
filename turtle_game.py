"""A turtle racing game"""

import sys

from race_meet import RaceMeet
# from turtle import Turtle


def main():
    """The main entry point for the turtle game"""
    race_meet = RaceMeet()
    print("Race name: {}".format(race_meet.name))
    print("Race length: {} metres".format(race_meet.length))
    print("Number of competitors: {}".format(race_meet.number_of_competitors))


if __name__ == '__main__':
    sys.exit(main())
