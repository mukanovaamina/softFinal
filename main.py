from recipe import Recipe, CulinaryProcess
from plov_builder import PlovBuilder
from manti_builder import MantiBuilder
from cook import Cook
from timer import Timer
from dumplings import Dumplings
from sauce_decorator import SauceDecorator
from cheese_decorator import CheeseDecorator
from cooking_context import CookingContext
from steaming_strategy import SteamingStrategy
from boiling_strategy import BoilingStrategy
from salt_command import SaltCommand
from pepper_command import PepperCommand
from culinary_expert import CulinaryExpert

def main():
    # Одиночка
    recipe_instance = Recipe()
    culinary_process = CulinaryProcess(recipe_instance)

    # Фабричный метод
    plov_builder = PlovBuilder()
    manti_builder = MantiBuilder()
    plov_dish = plov_builder.create_dish()
    manti_dish = manti_builder.create_dish()

    # Наблюдатель
    cooking_step = Dumplings()
    cook_observer = Cook()
    timer_observer = Timer()
    cooking_step.add_observer(cook_observer)
    cooking_step.add_observer(timer_observer)
    cooking_step.notify_observers()

    # Декоратор
    dumplings = Dumplings()
    sauce_dumplings = SauceDecorator(dumplings)
    cheese_sauce_dumplings = CheeseDecorator(sauce_dumplings)
    cheese_sauce_dumplings.prepare()

    # Стратегия
    steaming_strategy = SteamingStrategy()
    boiling_strategy = BoilingStrategy()
    cooking_context = CookingContext(steaming_strategy)
    cooking_context.cook()
    cooking_context.set_strategy(boiling_strategy)
    cooking_context.cook()

    # Команда
    salt_command = SaltCommand()
    pepper_command = PepperCommand()
    culinary_expert = CulinaryExpert()
    culinary_expert.execute_command(salt_command)
    culinary_expert.execute_command(pepper_command)

if __name__ == "__main__":
    main()
