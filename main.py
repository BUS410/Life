"""This is my little program that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

import pygame

from field import Field

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
FPS = 60
WINDOW_BORDER = 0
FULLSCREEN = 0  # 0 to non fullscreen

UI_WIDTH = 0

ROWS, COLS = 50, 80

# colors
BLACK = (0, 0, 0)


class Program:
    """The main class for playing a program"""

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              FULLSCREEN)
        pygame.display.set_caption('Life by BUS410')
        self.field = Field(SCREEN_WIDTH - UI_WIDTH - (WINDOW_BORDER * 2),
                           SCREEN_HEIGHT - (WINDOW_BORDER * 2), COLS, ROWS)
        self.field.update()
        self.clock = pygame.time.Clock()

    def main(self):
        while True:
            if not self.update():
                break
            self.clock.tick(FPS)
        pygame.quit()

    def update(self):
        next_update = True

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                next_update = False
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    next_update = False
                elif e.key == pygame.K_p:
                    self.field.put_food(COLS + ROWS)
                elif e.key == pygame.K_c:
                    self.field.clear()
                elif e.key == pygame.K_o:
                    self.field.put_live(1)
                elif e.key == pygame.K_u:
                    self.field.update()

        self.field.update()
        self.draw()

        return next_update

    def draw(self):
        self.window.fill(BLACK)
        self.field.draw(self.window, (WINDOW_BORDER + UI_WIDTH, WINDOW_BORDER))
        pygame.display.update()


if __name__ == '__main__':
    Program().main()
