is_food_regrows = True

SIZE = 100

AMOUNT = 250

STARTING_AMOUNT = 5000


food_locations = []

cell_locations = []

cells_amount = []

t_list = []

food = Food(10000)

t_list = [i for i in range(1, 41)]

cell_list = [Cell() for i in range(STARTING_AMOUNT)]

world = World(28, food, cell_list)
