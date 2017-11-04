"""A model of a race, all ready for the racing turtles to race in"""

from random import randint


class Race:
    def __init__(self):
        self.length = self.generate_length()
        self.number_of_competitors = self.generate_number_of_competitors()
        self.name = self.generate_race_name()

    def generate_length(self):
        return randint(1, 10)

    def generate_number_of_competitors(self):
        return randint(1, 5)

    def generate_place_name(self):
        with open('place_names.txt') as f:
            place_names = f.read().splitlines()

        return place_names[randint(0, len(place_names) - 1)]

    def generate_time(self):
        """Generates a time between 11:00 and 17:55, ensuring
        it's at a five minute increment"""
        hour = randint(11, 17)
        minute = int(5 * round(float(randint(0, 57)) / 5))
        return "{}:{:02}".format(hour, minute)

    def generate_race_name(self):
        """Generates a race name in the format 'HH:MM from <place_name>"""
        return "{} from {}".format(self.generate_time(),
                                   self.generate_place_name())
