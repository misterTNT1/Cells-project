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
