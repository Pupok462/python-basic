from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is not True:
            if self.fuel <= 0:
                raise LowFuelError
            self.started = True

    def move(self, distance):
        if self.fuel < distance * self.fuel_consumption:
            raise NotEnoughFuel
        self.fuel = self.fuel - distance * self.fuel_consumption
