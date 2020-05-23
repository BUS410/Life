"""This is my little module that mimics natural selection.
Python version 3.8.2, pygame version 1.9.6."""

import pygame

from .objects import Food, Organism
from .field import Field, Cell

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


class Program:
    """The main class for playing a program"""

    def __init__(self):
        pygame.init()

    def start(self):
        pass


if __name__ == '__main__':
    pass
