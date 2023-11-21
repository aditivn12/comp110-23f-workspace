class Bear:
   def __init__(self, age: int = 0, hunger_score: int = 0):
      self.age = age
      self.hunger_score = hunger_score
   def one_day(self):
      self.age += 1