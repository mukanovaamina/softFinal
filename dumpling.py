# dumplings.py
from dish import Dish

class Dumplings(Dish):
    def __init__(self, name):
        self.name = name
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def prepare(self):
        print(f"Preparing {self.name}")
        self.notify_observers()
