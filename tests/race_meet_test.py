"""The test scripts for the turtle class"""

from race_meet import RaceMeet


def test_generate_length_generates_valid_length():
    """Generates 20 numbers to try and ensure that all numbers are valid"""
    for i in range(0, 20):
        generated_length = RaceMeet().generate_length()
        assert generated_length >= 1
        assert generated_length <= 10


def test_generate_number_of_competitors_generates_valid_number():
    """Generates 20 numbers to try and ensure that all numbers are valid"""
    for i in range(0, 20):
        generated_number_of_competitors = (
            RaceMeet().generate_number_of_competitors()
        )
        assert generated_number_of_competitors >= 1
        assert generated_number_of_competitors <= 10


def test_generate_place_name_generates_valid_name():
    with open('place_names.txt') as f:
        place_names = f.read().splitlines()

    assert RaceMeet().generate_place_name() in place_names


def test_generate_time_generates_valid_time():
    """Generates 20 times to try and ensure that all times are valid"""
    for i in range(0, 20):
        generated_time = RaceMeet().generate_time()
        assert int(generated_time[0:2]) >= 11
        assert int(generated_time[0:2]) <= 17
        assert generated_time[2:3] == ":"
        assert int(generated_time[4:5]) in [0, 5]
        assert int(generated_time[3:5]) >= 0
        assert int(generated_time[3:5]) <= 55
