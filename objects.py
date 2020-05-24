from random import randint


MIN_ENERGY = 32
MAX_SPEED = 5
MAX_VR = 5
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

    def update(self):
        pass


class Organism:
    """An organism that will eat and breed"""

    def __init__(self, cell, energy: int, visibility_range: int, speed: int,
                 finicky: int):
        self.finicky = stabilize(finicky)
        self.speed = stabilize(speed, maximum=MAX_SPEED)
        self.visibility_range = stabilize(visibility_range, maximum=MAX_VR)
        self.energy = stabilize(energy, minimum=MIN_ENERGY)
        self.cell = cell
        self.color = (energy, 0, 255 - energy)
        self.is_organism = True

    def update(self, field):
        self.energy -= HUNGRY_SPEED
