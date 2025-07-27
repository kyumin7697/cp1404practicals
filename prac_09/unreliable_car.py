import random
from prac_09.car import Car

class UnreliableCar(Car):
    """An UnreliableCar has a reliability % chance of actually driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive. Only drive if random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0