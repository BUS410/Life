from random import randint

from pygame.draw import rect as draw_rect
from pygame.surface import Surface

from objects import Food, Organism

CELLS_COLOR = (128, 128, 128)
FIELD_COLOR = (64, 64, 64)


class Field:
    """Field consisting of cells"""

    def __init__(self, width: int, height: int, cols: int, rows: int,
                 border_width=1):
        self.height = height
        self.width = width
        self.surface = Surface((width, height))

        # creating field cells
        self._rows = [[] for _ in range(rows)]
        cell_width = width / cols
        cell_height = height / rows
        for y in range(rows):
            for x in range(cols):
                cell = Cell(self, (x, y), x * cell_width, y * cell_height,
                            cell_width, cell_height, border_width)
                self._rows[y].append(cell)

    def put_live(self, count):
        for i in range(count):
            y = randint(0, len(self._rows) - 1)
            x = randint(0, len(self._rows[0]) - 1)
            cell = self._rows[y][x]
            cell.obj = Organism(cell=cell,
                                energy=randint(1, 255),
                                visibility_range=randint(1, 5),
                                finicky=randint(1, 255))

    def put_food(self, count):
        for i in range(count):
            y = randint(0, len(self._rows) - 1)
            x = randint(0, len(self._rows[0]) - 1)
            cell = self._rows[y][x]
            cell.obj = Food(cell)

    def clear(self):
        for row in self._rows:
            for cell in row:
                cell.obj = None

    def update(self):
        self.surface.fill(FIELD_COLOR)
        for row in self._rows:
            for cell in row:
                cell.update()
        for row in self._rows:
            for cell in row:
                cell.set_not_updated()
                cell.draw()

    def change_border_cells(self, width: int):
        for row in self._rows:
            for cell in row:
                cell.border_width = width

    def draw(self, surface, pos: tuple = (0, 0)):
        surface.blit(self.surface, pos)

    def __getitem__(self, item):
        return self._rows[item]

    def __len__(self):
        return len(self._rows)

    def __str__(self):
        res = ''
        for row in self._rows:
            for cell in row:
                res += str(cell) + ' '
            res += '\n'
        return res


class Cell:
    """The cell for food and organisms of which the field will consist"""

    def __init__(self, filed: Field, pos: tuple, x, y, width, height,
                 border_width):
        self.pos = pos
        self.filed = filed
        assert width > border_width and height > border_width
        self.x = x + border_width
        self.y = y + border_width
        self.width = width - border_width
        self.height = height - border_width
        self.obj = None

    def put(self, obj):
        self.obj = obj

    def update(self):
        if self.obj and self.obj.is_organism and not self.obj.updated:
            self.obj.update(self.filed)

    def set_not_updated(self):
        if self.obj and self.obj.is_organism:
            self.obj.updated = False

    def __str__(self):
        return f'Cell<{self.x=}, {self.y=}, {self.width=}, {self.height=}>'

    def draw(self):
        draw_rect(self.filed.surface,
                  self.obj.color if self.obj else CELLS_COLOR,
                  (self.x, self.y, self.width, self.height))
