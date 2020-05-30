"""This is my little program that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

import pygame

from field import Field
from ui import Widget

FPS = 60
UPDATE_FREQUENCY = 4
UI_WIDTH = 200
MIN_ROWS_COLS = 3
WIDGET_HEIGHT = 50
WINDOW_BACKGROUND = (32, 32, 32)
BUTTON_COLOR = (72, 72, 72)
BUTTON_COVER = (64, 64, 64)
BUTTON_CLICKED = (128, 128, 128)


class Program:
    """The main class for playing a program"""

    def __init__(self, resolution=(1280, 720),
                 fullscreen=True):
        pygame.init()
        fullscreen = pygame.FULLSCREEN if fullscreen else 0
        self.resolution = resolution
        self.window = pygame.display.set_mode(resolution, fullscreen)
        pygame.display.set_caption('Life by BUS410')
        self.cols = resolution[0] // 20
        self.rows = resolution[1] // 20
        self.field = Field(resolution[0] - UI_WIDTH, resolution[1], self.cols,
                           self.rows)
        self.field.update()
        self.update_iterator = UPDATE_FREQUENCY
        self.update_frequency = UPDATE_FREQUENCY
        self.clock = pygame.time.Clock()
        self.start = False
        self.next_update = True
        self.widgets = [
            Widget(x=0,
                   y=0,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Старт/Стоп',
                   background_color=BUTTON_COLOR,
                   onclick=self.start_stop,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=WIDGET_HEIGHT,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Очистить',
                   onclick=self.clear,
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 2,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Размер таблицы'),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 3,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='-',
                   onclick=lambda: self.change_field('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=WIDGET_HEIGHT * 3,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT, text='+',
                   onclick=lambda: self.change_field('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 4,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='-10',
                   onclick=lambda: self.change_field('-', 10),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=WIDGET_HEIGHT * 4,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='+10',
                   onclick=lambda: self.change_field('+', 10),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 5,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Частота обновл.'),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 6,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='-',
                   onclick=lambda: self.change_update_frequency('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=WIDGET_HEIGHT * 6,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT, text='+',
                   onclick=lambda: self.change_update_frequency('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 7,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Еды за раз'),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 8,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='-',
                   onclick=lambda: self.change_food_count('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=WIDGET_HEIGHT * 8,
                   width=UI_WIDTH // 2,
                   height=WIDGET_HEIGHT,
                   text='+',
                   onclick=lambda: self.change_food_count('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),

            Widget(x=0,
                   y=WIDGET_HEIGHT * 9,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Пищи: 1'),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 10,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Организмов: 0'),
            Widget(x=0,
                   y=WIDGET_HEIGHT * 11,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Хищников: 0'),

            Widget(x=0,
                   y=resolution[1] - WIDGET_HEIGHT,
                   width=UI_WIDTH,
                   height=WIDGET_HEIGHT,
                   text='Выход',
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED,
                   onclick=self.quit)
        ]

    def start_stop(self):
        if self.start:
            self.start = False
        else:
            self.start = True

    def quit(self):
        self.next_update = False

    def clear(self):
        self.field.clear()
        self.field.update()

    def change_food_count(self, action):
        if action == '+':
            self.field.count_put_food += 1
        elif action == '-':
            if self.field.count_put_food > 0:
                self.field.count_put_food -= 1

    def change_update_frequency(self, action):
        if action == '+':
            self.update_frequency += 1
            if self.update_frequency >= FPS:
                self.update_frequency = FPS
        elif action == '-':
            self.update_frequency -= 1
            if self.update_frequency <= 1:
                self.update_frequency = 1

    def change_field(self, action, n=1):
        if action == '+':
            self.rows += n
            self.cols += n
        elif action == '-':
            if self.rows > MIN_ROWS_COLS + n - 1:
                self.rows -= n
            if self.cols > MIN_ROWS_COLS + n - 1:
                self.cols -= n
        self.field = Field(self.resolution[0] - UI_WIDTH, self.resolution[1],
                           self.cols, self.rows,
                           count_put_food=self.field.count_put_food)
        self.field.update()

    def update_info(self):
        self.widgets[-2].text = f'Хищников: {self.field.predators}'
        self.widgets[-3].text = f'Организмов: {self.field.organisms}'
        self.widgets[-4].text = f'Пищи: {self.field.foods}'

    def main(self):
        while True:
            if not self.update():
                break
            self.clock.tick(FPS)
        pygame.quit()

    def update(self):
        self.next_update = True
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                self.next_update = False
            elif e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE:
                self.next_update = False
            elif e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > UI_WIDTH:
                        pos = (pos[0] - UI_WIDTH, pos[1])
                        self.field.put_live(1, pos)
                        self.field.update()
                        self.update_info()

        for widget in self.widgets:
            widget.update(events)

        if self.start and not self.update_iterator:
            self.update_iterator = self.update_frequency
            self.field.update()
            self.update_info()
        if self.update_iterator:
            self.update_iterator -= 1

        self.draw()

        return self.next_update

    def draw(self):
        self.window.fill(WINDOW_BACKGROUND)
        for widget in self.widgets:
            widget.show(self.window)
        self.field.draw(self.window, (UI_WIDTH, 0))
        pygame.display.update()


class Menu:
    pass


if __name__ == '__main__':
    Program().main()
