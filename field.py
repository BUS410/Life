from pygame import draw
from pygame.surface import Surface

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
                cell = Cell(self, x * cell_width, y * cell_height, cell_width,
                            cell_height, border_width)
                self._rows[y].append(cell)

    def update(self):
        self.surface.fill(FIELD_COLOR)
        for row in self._rows:
            for cell in row:
                cell.update()
                cell.draw()

    def get_objects(self):
        res = []
        for i, row in enumerate(self._rows):
            res.append([])
            for cell in row:
                res[i].append(cell.obj)
        return res

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

    def __iter__(self):
        for row in self._rows:
            yield row

    def __str__(self):
        res = ''
        for row in self._rows:
            for cell in row:
                res += str(cell) + ' '
            res += '\n'
        return res


class Cell:
    """The cell for food and organisms of which the field will consist"""

    def __init__(self, filed: Field, x, y, width, height, border_width: int):
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
        if self.obj:
            self.obj.update()

    def __str__(self):
        return f'Cell<{self.x=}, {self.y=}, {self.width=}, {self.height=}>'

    def draw(self):
        draw.rect(self.filed.surface, CELLS_COLOR,
                  (self.x, self.y, self.width, self.height))
