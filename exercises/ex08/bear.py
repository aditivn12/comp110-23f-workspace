"""Defines bear class."""


class Bear:
    """Bear class function."""
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Initilizing function for the bear with age and hunger score."""
        self.age = age
        self.hunger_score = hunger_score

    def one_day(self):
        """A bear's life in one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, amount):
        """Function for the bear eating."""
        self.hunger_score += amount