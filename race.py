"""An actual race"""


class Race:
    def get_time_for_turtle_over_next_metre(self, speed):
        speed_per_minute = 0.1 * speed  # i.e. turtle covers this over 1 minute
        return round((1 / speed_per_minute) * 60)

    def get_energy_for_turtle_after_next_metre(self, start_energy, stamina):
        energy_used_per_metre = 10 + (10 - stamina)
        return start_energy - energy_used_per_metre

    def get_new_turtle_speed(self, current_speed, energy_before_metre,
                             energy_after_metre):
        if ((energy_before_metre >= 80) and (energy_after_metre < 80) or
           (energy_before_metre >= 60) and (energy_after_metre < 60) or
           (energy_before_metre >= 40) and (energy_after_metre < 40) or
           (energy_before_metre >= 20) and (energy_after_metre < 20)):
            new_speed = current_speed - 1
        else:
            new_speed = current_speed
        return new_speed

    def get_total_time_for_turtle(self, speed, stamina, length):
        energy = 100
        total_time = 0
        for current_metre in range(1, length + 1):
            total_time += self.get_time_for_turtle_over_next_metre(speed)
            new_energy = self.get_energy_for_turtle_after_next_metre(energy,
                                                                     stamina)
            speed = self.get_new_turtle_speed(speed, energy, new_energy)
            energy = new_energy
        if energy <= 0:
            total_time = 0
        return total_time
