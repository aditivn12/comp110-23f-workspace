"""Defines fish class."""


class Fish:
    """A fish object is created."""
    age = int

    def __init__(self, age: int = 0):
        """A fish object is made."""
        self.age = age

    def one_day(self):
        """Simulates on day for a fish."""
        self.age += 1