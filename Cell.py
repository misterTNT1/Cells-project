class Cell:
  def __init__(self):
    self.location = gen_location(cell_locations)

  def move(self):
    new_location = self.food_nearby()
    if new_location is None:
      x, y = randint(-1, 1), randint(-1, 1)
      while abs(self.location[0] + x) > 50:
        x, y = randint(-1, 1), randint(-1, 1)
        if [self.location[0] + x, self.location[1] +  y] in cell_locations:
          x, y = randint(-1, 1), randint(-1, 1)
      self.location[0] += x
      self.location[1] += y

  def check_for_food(self):
    location = self.location
    return location if location in food_locations else None


  def gen_locations(self):
    while len(cell_locations) < STARTING_AMOUNT:
      location = gen_location(cell_locations)
      if location:
        cell_locations.append(gen_location(cell_locations))


  def food_nearby(self):
    for x in [self.location[0] - 1, self.location[0] + 1]:
      for y in [self.location[1] - 1, self.location[1] + 1]:
        if [x, y] in food_locations:
          return [x, y]

    return None
