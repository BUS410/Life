"""This is my little program that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

import pygame

from field import Field
from ui import Widget

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60
UPDATE_FREQUENCY = 5
UI_WIDTH = 200
ROWS, COLS = SCREEN_HEIGHT//20, (SCREEN_WIDTH - UI_WIDTH)//20
MIN_ROWS_COLS = 3
BUTTON_H = 50
WINDOW_BACKGROUND = (0, 0, 0)
BUTTON_COLOR = (72, 72, 72)
BUTTON_COVER = (64, 64, 64)
BUTTON_CLICKED = (128, 128, 128)

# 0 to non fullscreen, pygame.FULLSCREEN to fullscreen
FULLSCREEN = pygame.FULLSCREEN


class Program:
    """The main class for playing a program"""

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              FULLSCREEN)
        pygame.display.set_caption('Life by BUS410')
        self.cols = COLS
        self.rows = ROWS
        self.field = Field(SCREEN_WIDTH - UI_WIDTH, SCREEN_HEIGHT, COLS, ROWS)
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
                   height=BUTTON_H,
                   text='Старт/Стоп',
                   onclick=self.start_stop,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=BUTTON_H,
                   width=UI_WIDTH,
                   height=BUTTON_H,
                   text='Очистить',
                   onclick=self.clear,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=BUTTON_H * 2,
                   width=UI_WIDTH,
                   height=BUTTON_H,
                   text='Размер таблицы'),
            Widget(x=0,
                   y=BUTTON_H * 3,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H,
                   text='-',
                   onclick=lambda: self.change_field('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=BUTTON_H * 3,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H, text='+',
                   onclick=lambda: self.change_field('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=BUTTON_H * 4,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H,
                   text='-10',
                   onclick=lambda: self.change_field('-', 10),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=BUTTON_H * 4,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H,
                   text='+10',
                   onclick=lambda: self.change_field('+', 10),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=BUTTON_H * 5,
                   width=UI_WIDTH,
                   height=BUTTON_H,
                   text='Частота обновл.'),
            Widget(x=0,
                   y=BUTTON_H * 6,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H,
                   text='-',
                   onclick=lambda: self.change_update_frequency('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=BUTTON_H * 6,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H, text='+',
                   onclick=lambda: self.change_update_frequency('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=0,
                   y=BUTTON_H * 7,
                   width=UI_WIDTH,
                   height=BUTTON_H,
                   text='Еды за раз'),
            Widget(x=0,
                   y=BUTTON_H * 8,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H,
                   text='-',
                   onclick=lambda: self.change_food_count('-'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),
            Widget(x=UI_WIDTH // 2,
                   y=BUTTON_H * 8,
                   width=UI_WIDTH // 2,
                   height=BUTTON_H, text='+',
                   onclick=lambda: self.change_food_count('+'),
                   background_color=BUTTON_COLOR,
                   background_color_cover=BUTTON_COVER,
                   background_color_click=BUTTON_CLICKED),

            Widget(x=0,
                   y=SCREEN_HEIGHT-BUTTON_H,
                   width=UI_WIDTH,
                   height=BUTTON_H,
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
        self.field = Field(SCREEN_WIDTH - UI_WIDTH, SCREEN_HEIGHT,
                           self.cols, self.rows)
        self.field.update()

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
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    self.next_update = False
                elif e.key == pygame.K_p:
                    self.field.put_food(COLS + ROWS)
                    self.field.update()
                elif e.key == pygame.K_c:
                    self.clear()
                elif e.key == pygame.K_o:
                    self.field.put_live(1)
                elif e.key == pygame.K_u:
                    self.field.update()
                elif e.key == pygame.K_s:
                    self.start_stop()
            elif e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > UI_WIDTH:
                        pos = (pos[0] - UI_WIDTH, pos[1])
                        self.field.put_live(1, pos)
                        self.field.update()

        for widget in self.widgets:
            widget.update(events)

        if self.start and not self.update_iterator:
            self.update_iterator = self.update_frequency
            self.field.update()
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


if __name__ == '__main__':
    Program().main()
