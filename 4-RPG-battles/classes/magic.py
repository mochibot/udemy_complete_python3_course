import random


class Spell:
  def __init__(self, name, cost, damage, type):
    self.name = name
    self.cost = cost
    self.damage = damage
    self.type = type

  def generate_damage(self):
    lo = self.damage - 15
    hi = self.damage + 15
    return random.randrange(lo, hi)
