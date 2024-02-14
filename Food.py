from random import random, randint

def gen_location(l1, size=SIZE): #this is the same function that is in Cell.py
  if l1 is food_locations:
    location = [randint(-size / 2, size /2 ), randint(-size / 2, size / 2)]
    while location in food_locations:
      location = [randint(-size / 2, size /2 ), randint(-size / 2, size / 2)]
    food_locations.append(location)
  else:
    location = [randint(-size / 2, size /2 ), randint(-size / 2, size / 2)]
    while location in cell_locations:
      location = [randint(-size / 2, size /2 ), randint(-size / 2, size / 2)]
    cell_locations.append(location)
  return location

class Food:
  global AMOUNT
  def __init__(self, food_per_t):
    global food_list
    self.locations = []
    self.food_per_t = food_per_t
    self.is_food_regrows = is_food_regrows


  def gen_locations(self):
    while len(food_locations) < AMOUNT:
      location = gen_location(food_locations)
      food_locations.append(location)
