from . import pygame

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
