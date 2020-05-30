from math import ceil
from random import randint, choice

MIN_ENERGY = 64
MAX_ENERGY = 255
FOOD_ENERGY_FACTOR = 0.1
MAX_VR = 5
MIN_VR = 1
HUNGRY_SPEED = 2
PREDATOR_PROBABILITY = 100


def stabilize(n, maximum=MAX_ENERGY, minimum=1):
    if n > maximum:
        n = maximum
    elif n < minimum:
        n = minimum
    return n


class Food:
    """The food that organisms will eat"""

    def __init__(self, cell):
        self.cell = cell
        self.energy = randint(MIN_ENERGY, MAX_ENERGY)
        self.is_organism = False
        self.predator = True  # food not for predator

        # color will depend on the amount of energy in food
        self.color = (self.energy, self.energy, 0)
        self.updated = None


class Organism:
    """An organism that will eat and breed"""

    def __init__(self, cell, energy: int, visibility_range: int, finicky: int,
                 predator=False):
        self.finicky = stabilize(finicky)
        self.visibility_range = stabilize(visibility_range, MAX_VR, MIN_VR)
        self.energy = stabilize(energy, minimum=MIN_ENERGY)
        self.cell = cell
        self.color = (energy, 0, MAX_ENERGY - energy)
        self.is_organism = True
        self.updated = False
        self.predator = predator

    def die(self):
        self.cell.put(None)

    def birth_new(self, pos):
        predator = False
        if self.predator:
            predator = True
        else:
            if randint(0, PREDATOR_PROBABILITY) == 0:
                predator = True
        energy = self.energy = ceil(self.energy / 2)
        visibility_range = self.visibility_range + randint(-1, 1)
        visibility_range = stabilize(visibility_range, MAX_VR, MIN_VR)
        finicky = self.finicky + randint(-MAX_ENERGY // 10, MAX_ENERGY // 10)
        finicky = stabilize(finicky)
        organism = Organism(cell=self.cell.filed[pos[1]][pos[0]],
                            energy=energy, visibility_range=visibility_range,
                            finicky=finicky, predator=predator)
        return organism

    def update(self):
        field = self.cell.filed
        self.energy -= HUNGRY_SPEED
        self.color = (255 if self.predator else 0, self.finicky, self.energy)
        if self.energy <= 0:
            self.die()
            return
        cells_with_food = []
        empty_cells = []
        h, w = len(field), len(field[0])
        for y in range(max(0, self.cell.pos[1] - self.visibility_range),
                       min(self.cell.pos[1] + self.visibility_range + 1, h)):
            for x in range(max(0, self.cell.pos[0] - self.visibility_range),
                           min(self.cell.pos[0] + self.visibility_range + 1,
                               w)):
                cell = field[y][x]
                if (self.predator and cell.obj and
                        not cell.obj.predator and
                        self.finicky <= cell.obj.energy):
                    cells_with_food.append(cell)
                    print(cell.obj)
                elif (type(cell.obj) is Food and self.finicky <= cell.obj.energy
                      and not self.predator):
                    cells_with_food.append(cell)
                elif type(cell.obj) is not Organism:
                    empty_cells.append(cell)
        if cells_with_food:
            new_cell = choice(cells_with_food)
            self.energy += round(new_cell.obj.energy * FOOD_ENERGY_FACTOR)
            self.energy = min(MAX_ENERGY, self.energy)
        elif empty_cells:
            new_cell = choice(empty_cells)
        else:
            return

        if self.energy == MAX_ENERGY:
            obj = self.birth_new(self.cell.pos)
        else:
            obj = None

        old_pos = self.cell.pos
        new_pos = new_cell.pos
        field[old_pos[1]][old_pos[0]].put(obj)
        field[new_pos[1]][new_pos[0]].put(self)
        self.cell = field[new_pos[1]][new_pos[0]]

        self.updated = True
