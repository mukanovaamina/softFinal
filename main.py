from recipe import Recipe
from culinary_process import CulinaryProcess
from plov_builder import PlovBuilder
from plov import Plov
from manti_builder import MantiBuilder
from manti import Manti
from cook import Cook
from timer import Timer
from dumpling import Dumplings
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
    recipe_instance = Recipe()  # Создание единственного экземпляра рецепта
    culinary_process = CulinaryProcess(recipe_instance)

    # Фабричный метод
    plov_builder = PlovBuilder()
    manti_builder = MantiBuilder()
    plov_dish = plov_builder.create_dish()  # Создание блюда с использованием фабричного метода
    manti_dish = manti_builder.create_dish()
    manti_instance = Manti()
    manti_instance.prepare()
    plov_instance = Plov()
    plov_instance.prepare()  # Добавлен вызов метода prepare для Plov
    dumplings_instance = Dumplings(name="Dumplings")
    dumplings_instance.prepare()

    # Наблюдатель
    cooking_step = Dumplings(name="Dumplings")  # Создание экземпляра Dumplings с указанием имени
    cook_observer = Cook()
    timer_observer = Timer()
    cooking_step.add_observer(cook_observer)
    cooking_step.add_observer(timer_observer)
    cooking_step.notify_observers()

    # Декоратор
    dumplings = Dumplings(name="Dumplings")  # Создание экземпляра Dumplings с указанием имени
    sauce_dumplings = SauceDecorator(dumplings)  # Декорирование Dumplings с соусом
    cheese_sauce_dumplings = CheeseDecorator(sauce_dumplings)  # Декорирование Dumplings с соусом и сыром
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
