# manti.py
from dish import Dish

class Manti(Dish):
    def __init__(self, name="Manti"):
        super().__init__(name)

    def prepare(self):
        print(f"Preparing {self.name}")
