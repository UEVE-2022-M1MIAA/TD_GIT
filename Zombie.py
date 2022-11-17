import random

class Zombie:
  def __init__(self):
    self.degat = random.choice([1, 2])
    self.loot = random.choice([0.5, 1])
    