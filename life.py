"""This is my little module that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

from random import randint

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

CELLS_COLOR = (255, 255, 255)


class Field:
    """Field consisting of cells"""

    def __init__(self, width: int, height: int, cols: int, rows: int):
        self.height = height
        self.width = width
        self.surface = pygame.Surface((width, height))

        # creating field cells
        self._rows = [[] for _ in range(rows)]
        cell_width = width // cols
        cell_height = height // rows
        for y in range(rows):
            for x in range(cols):
                cell = Cell(x * cell_width, y * cell_width, cell_width,
                            cell_height)
                self._rows[y].append(cell)

    def update(self):
        pass

    def draw(self, surface: pygame.Surface, pos: tuple = (0, 0)):
        surface.blit(self.surface, pos)

    def __getitem__(self, item):
        return self._rows[item]

    def __len__(self):
        return len(self._rows)

    def __iter__(self):
        for row in self._rows:
            yield row


class Cell:
    """The cell for food and organisms of which the field will consist"""

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.obj = None

    def put(self, obj):
        self.obj = obj

    @property
    def is_empty(self):
        return self.obj

    def __str__(self):
        return f'Cell<{self.x=}, {self.y=}, {self.width=}, {self.height=}>'

    def draw(self, filed: Field):
        pygame.draw.rect(filed, CELLS_COLOR,
                         (self.x, self.y, self.width, self.height))


class Food:
    """The food that organisms will eat"""

    def __init__(self, x: int, y: int, energy: int = None):
        self.pos = [x, y]
        self.energy = energy or randint(0, 255)
        assert 0 < energy <= 255

        # color will depend on the amount of energy in food
        self.color = (energy, 0, 255 - energy)

    def draw(self, surface: pygame.Surface, cell: Cell):
        pass

    def __bool__(self):
        return True


class Organism:
    """An organism that will eat and breed"""

    def __init__(self):
        pass

    def update(self, field: Field):
        pass

    def draw(self, surface: pygame.Surface, cell):
        pass

    def __bool__(self):
        return True


class Program:
    """The main class for playing a program"""

    def __init__(self):
        pygame.init()

    def start(self):
        pass


if __name__ == '__main__':
    pass
