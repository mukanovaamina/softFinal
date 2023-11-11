from observer import Observer

class Cook(Observer):
    def update(self, cooking_step):
        print(f"Cooking step completed: {cooking_step.name}")
