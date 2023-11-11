from dish import Dish

class Decorator(Dish):
    def __init__(self, dish):
        self._dish = dish

    def prepare(self):
        self._dish.prepare()
