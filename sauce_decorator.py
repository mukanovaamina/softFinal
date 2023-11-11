from decorator import Decorator

class SauceDecorator(Decorator):
    def prepare(self):
        super().prepare()
        print("Adding Sauce")
