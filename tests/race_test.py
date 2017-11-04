"""The test scripts for the Race class"""

import pytest

from race import Race


@pytest.fixture
def race():
    return Race()


def test_get_example_turtle_1_stats_after_metre(race):
    """Turtle 1 has speed of 4 and stamina of 5"""
    assert race.get_time_for_turtle_over_next_metre(4) == 150


def test_get_example_turtle_1_energy_after_metre(race):
    """Turtle 1 has speed of 4 and stamina of 5"""
    assert race.get_energy_for_turtle_after_next_metre(100, 5) == 85


def test_get_examle_turtle_1_finishing_time(race):
    """Turtle 1 has speed of 4 and stamina of 5 and race is 6m"""
    assert race.get_total_time_for_turtle(4, 5, 6) == 1700


def test_get_example_turtle_2_stats_after_metre(race):
    """Turtle 1 has speed of 7 and stamina of 8"""
    assert race.get_time_for_turtle_over_next_metre(7) == 86


def test_get_exmaple_turtle_2_stats_after_metre(race):
    """Turtle 1 has speed of 7 and stamina of 8"""
    assert race.get_energy_for_turtle_after_next_metre(100, 8) == 88


def test_get_examle_turtle_2_finishing_time(race):
    """Turtle 1 has speed of 7 and stamina of 8 and race is 6m"""
    assert race.get_total_time_for_turtle(7, 8, 6) == 612


def test_get_new_turtle_speed(race):
    """Turtle has current energy of 59 after previously having 69
    and has a current speed of 6"""
    assert race.get_new_turtle_speed(6, 69, 59) == 5
