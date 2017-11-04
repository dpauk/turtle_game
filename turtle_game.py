"""A turtle racing game"""

import sys

from race_meet import RaceMeet
from turtle import Turtle


def generate_competitor_list(number_of_competitors):
    """Generates a list of the competitors"""
    competitor_list = []
    for i in range(0, number_of_competitors):
        competitor_list.append(Turtle())
    return competitor_list


def main():
    """The main entry point for the turtle game"""
    race_meet = RaceMeet()
    print("Race name: {}".format(race_meet.name))
    print("Race length: {} metres".format(race_meet.length))
    print("Number of competitors: {}\n".format(race_meet.number_of_competitors))

    competitors = generate_competitor_list(race_meet.number_of_competitors)

    for i in range(0, len(competitors)):
        print("Competitor {}: {}".format(i + 1, competitors[i].name))


if __name__ == '__main__':
    sys.exit(main())
