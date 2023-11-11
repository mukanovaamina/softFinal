from decorator import Decorator

class CheeseDecorator(Decorator):
    def prepare(self):
        super().prepare()
        print("Adding Cheese")
