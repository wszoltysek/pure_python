class Car:
    def __init__(self, pax_count: int, car_mass: int, gear_count: int):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    @property
    def pax_count(self):
        return self._pax_count

    @pax_count.setter
    def pax_count(self, value: int):
        if value < 1:
            raise IllegalCarError("No passengers")
        elif value > 5:
            raise IllegalCarError("To many passengers")
        else:
            self._pax_count = value

    @property
    def car_mass(self):
        return self._car_mass

    @car_mass.setter
    def car_mass(self, value: int):
        if value > 2000:
            raise IllegalCarError("Car is to heavy")
        else:
            self._car_mass = value

    @property
    def total_mass(self):
        return self.car_mass + self.pax_count * 70


class IllegalCarError(ValueError):
    pass
