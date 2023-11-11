class Recipe:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Recipe, cls).__new__(cls)
        return cls._instance
