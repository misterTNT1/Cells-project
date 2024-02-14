class World:
  global STARTING_AMOUNT
  def __init__(self, temperature, food, cells: list):
    self.temperature = temperature
    self.starting_amount = STARTING_AMOUNT
    self.current_amount = self.starting_amount
    self.food = food
    self.cells = cells
    self.per_over_29 = 0.1
    self.size = SIZE
    self.per_temp_until_29 = 0.05
    self.current_percent = 0.1 - (self.temperature - 29 if self.temperature > 29 else 0) * self.per_over_29 + (temperature - 21) * self.per_temp_until_29


  def steps(self, n):
    for i in range(n):
      self.cells.append(Cell() for i in range(self.current_amount - STARTING_AMOUNT))
      cells_amount.append(self.current_amount)
      for cell in self.cells:
        if isinstance(cell, Generator):
          raise ValueError("a problem has occurred with the cell")
        num = random()
        if num < self.current_percent:
          current_location = cell.check_for_food()
          if current_location is not None:
            food_locations.remove(current_location)
            gen_location(cell_locations)
            self.current_amount += 1
          else:
            cell.move()
        else:
          cell_locations.remove(cell.location)
          self.cells.remove(cell)
          self.current_amount -= 1
      AMOUNT = len(food_locations) + food.food_per_t
      food.gen_locations()
