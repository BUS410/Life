from random import randint, choice


MIN_ENERGY = 32
MAX_VR = 5
MIN_VR = 2
HUNGRY_SPEED = 10


def stabilize(n, maximum=255, minimum=1):
    if n > maximum:
        n = maximum
    elif n < minimum:
        n = minimum
    return n


class Food:
    """The food that organisms will eat"""

    def __init__(self, cell):
        self.cell = cell
        self.energy = randint(MIN_ENERGY, 255)
        self.is_organism = False

        # color will depend on the amount of energy in food
        self.color = (0, self.energy, 0)
        self.updated = None

    def update(self):
        pass


class Organism:
    """An organism that will eat and breed"""

    def __init__(self, cell, energy: int, visibility_range: int, finicky: int):
        self.finicky = stabilize(finicky)
        self.visibility_range = stabilize(visibility_range, MAX_VR, MIN_VR)
        self.energy = stabilize(energy, minimum=MIN_ENERGY)
        self.cell = cell
        self.color = (energy, 0, 255 - energy)
        self.is_organism = True
        self.updated = False

    def update(self, field):
        self.energy -= HUNGRY_SPEED
        cells_with_food = []
        empty_cells = []
        h, w = len(field) - 1, len(field[0]) - 1
        for y in range(max(0, self.cell.pos[1] - self.visibility_range),
                       min(self.cell.pos[1] + self.visibility_range+1, h)):
            for x in range(max(0, self.cell.pos[0] - self.visibility_range),
                           min(self.cell.pos[0] + self.visibility_range+1, w)):
                cell = field[y][x]
                if type(cell.obj) is Food:
                    cells_with_food.append(cell)
                elif type(cell.obj) is not Organism:
                    empty_cells.append(cell)
        if cells_with_food:
            new_cell = choice(cells_with_food)
            self.energy += new_cell.obj.energy//2
        elif empty_cells:
            new_cell = choice(empty_cells)
        else:
            return

        old_pos = self.cell.pos
        new_pos = new_cell.pos
        field[old_pos[1]][old_pos[0]].put(None)
        field[new_pos[1]][new_pos[0]].put(self)
        self.cell = field[new_pos[1]][new_pos[0]]
        print(new_pos)

        self.updated = True

    def __bool__(self):
        return True
