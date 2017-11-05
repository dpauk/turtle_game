"""A turtle racing game"""

import sys

from race import Race
from race_meet import RaceMeet
from turtle import Turtle
from turtle_has_no_energy_error import TurtleHasNoEnergyError


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
    print(
        "Number of competitors: {}\n".format(race_meet.number_of_competitors)
    )

    competitors = generate_competitor_list(race_meet.number_of_competitors)

    race = Race()
    competitor_times = {}

    for i in range(0, len(competitors)):
        try:
            total_time_for_competitor = (
                race.get_total_time_for_turtle(competitors[i].speed,
                                               competitors[i].stamina,
                                               race_meet.length)
            )
        except TurtleHasNoEnergyError:
            print(
                ("Competitor {}: {} didn't have the energy to complete the "
                 "race...").format(i + 1, competitors[i].name)
            )
            continue
        competitor_times[competitors[i].name] = total_time_for_competitor
        print(
            ("Competitor {}: "
             "{} ran the race in {} seconds").format(i + 1,
                                                     competitors[i].name,
                                                     total_time_for_competitor)
        )


if __name__ == '__main__':
    sys.exit(main())
