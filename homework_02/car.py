"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    engine = []

    def set_engine(self, value):
        self.engine = value
        print(self.engine)






