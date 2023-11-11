from observer import Observer

class Timer(Observer):
    def update(self, cooking_step):
        print(f"Timer finished for cooking step: {cooking_step.name}")
