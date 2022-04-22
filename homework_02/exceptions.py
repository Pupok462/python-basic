"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """ Raised when Fuel < value"""
    pass


class NotEnoughFuel(Exception):
    """ Raised when Fuel not Enough to do smth"""
    pass


class CargoOverload(Exception):
    """ When car have more weight then needed """
    pass
