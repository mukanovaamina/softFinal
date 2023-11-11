from dish_builder import DishBuilder
from plov import Plov

class PlovBuilder(DishBuilder):
    def create_dish(self):
        return Plov()