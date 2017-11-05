"""The test scripts for the Race class"""

import pytest

from race import Race
from turtle_has_no_energy_error import TurtleHasNoEnergyError


@pytest.fixture
def race():
    return Race()


def test_get_example_turtle_1_stats_after_metre(race):
    """Turtle 1 has speed of 4 and stamina of 5"""
    assert race.get_time_for_turtle_over_next_metre(4) == 150


def test_get_example_turtle_1_energy_after_metre(race):
    """Turtle 1 has speed of 4 and stamina of 5"""
    assert race.get_energy_for_turtle_after_next_metre(100, 5) == 85


def test_get_example_turtle_1_finishing_time(race):
    """Turtle 1 has speed of 4 and stamina of 5 and race is 6m"""
    assert race.get_total_time_for_turtle(4, 5, 6) == 1700


def test_get_example_turtle_2_stats_after_metre(race):
    """Turtle 2 has speed of 7 and stamina of 8"""
    assert race.get_time_for_turtle_over_next_metre(7) == 86


def test_get_example_turtle_2_energy_after_metre(race):
    """Turtle 2 has speed of 7 and stamina of 8"""
    assert race.get_energy_for_turtle_after_next_metre(100, 8) == 88


def test_get_example_turtle_2_finishing_time(race):
    """Turtle 2 has speed of 7 and stamina of 8 and race is 6m"""
    assert race.get_total_time_for_turtle(7, 8, 6) == 612


def test_get_example_turtle_3_stats_after_metre(race):
    """Turtle 3 has speed of 1 and stamina of 1 - he's a no hoper..."""
    assert race.get_time_for_turtle_over_next_metre(1) == 600


def test_get_example_turtle_3_energy_after_metre(race):
    """Turtle 3 has speed of 1 and stamina of 1"""
    assert race.get_energy_for_turtle_after_next_metre(100, 1) == 81


def test_get_example_turtle_3_finishing_time(race):
    """Turtle 3 has speed of 1 and stamina of 1 and race is 6m"""
    # i.e. turtle never finishes
    with pytest.raises(TurtleHasNoEnergyError):
        race.get_total_time_for_turtle(1, 1, 6)


def test_get_new_turtle_speed(race):
    """Turtle has current energy of 59 after previously having 69
    and has a current speed of 6"""
    assert race.get_new_turtle_speed(6, 69, 59) == 5
