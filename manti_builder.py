# manti_builder.py
from dish_builder import DishBuilder
from manti import Manti

class MantiBuilder(DishBuilder):
    def create_dish(self):
        return Manti()
