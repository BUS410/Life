from random import randint

from . import pygame


class Food:
    """The food that organisms will eat"""

    def __init__(self, x: int, y: int, energy: int = None):
        self.pos = [x, y]
        self.energy = energy or randint(0, 255)
        assert 0 < energy <= 255

        # color will depend on the amount of energy in food
        self.color = (energy, 0, 255 - energy)

    def draw(self, surface: pygame.Surface, cell):
        pass

    def __bool__(self):
        return True


class Organism:
    """An organism that will eat and breed"""

    def __init__(self):
        pass

    def update(self, field):
        pass

    def draw(self, surface: pygame.Surface, cell):
        pass

    def __bool__(self):
        return True
