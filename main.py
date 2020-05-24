"""This is my little module that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

import pygame

from field import Field

SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
FULLSCREEN = pygame.FULLSCREEN  # 0 to non fullscreen

# colors
BLACK = (0, 0, 0)


class Program:
    """The main class for playing a program"""

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                              FULLSCREEN)
        pygame.display.set_caption('Life by BUS410')
        self.field = Field(SCREEN_WIDTH, SCREEN_HEIGHT, 50, 50)

    def main(self):
        while True:
            if not self.update():
                break
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
        self.field.update()
        self.draw()

        return next_update

    def draw(self):
        self.window.fill(BLACK)
        self.field.draw(self.window)
        pygame.display.update()


if __name__ == '__main__':
    Program().main()
