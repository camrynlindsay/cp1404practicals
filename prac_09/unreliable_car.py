import random  # Randint to determine reliability in drive method
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a specified distance only if the car is reliable."""
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
