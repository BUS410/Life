from pygame.mouse import (get_pos as get_mouse_pos,
                          get_pressed as get_mouse_pressed)
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import SysFont
from pygame import MOUSEBUTTONUP


class Widget:
    def __init__(self, **kwargs):
        self.rect = Rect(kwargs.get('x', 0),
                         kwargs.get('y', 0),
                         kwargs.get('width', 200),
                         kwargs.get('height', 50))
        self.image = Surface((self.rect.width, self.rect.height))
        self.background_image = kwargs.get('background_image', 0)
        self.background_image_pos = kwargs.get('background_image_pos', (0, 0))
        self.background_color = kwargs.get('background_color', (32, 32, 32))
        self.background_color_cover = kwargs.get('background_color_cover',
                                                 self.background_color)
        self.background_color_click = kwargs.get('background_color_click',
                                                 self.background_color)
        self.text = kwargs.get('text', '')
        self.font_size = kwargs.get('font_size', 20)
        self.font_color = kwargs.get('font_color', (255, 255, 255))
        self.font_pos = kwargs.get('font_pos', None)
        self.font = SysFont('segoeui', self.font_size, 1)
        self.image.fill(self.background_color)
        self.onclick = kwargs.get('onclick', lambda: None)

    def show(self, surface):
        if self.background_image:
            self.image.blit(self.background_image, self.background_image_pos)
        font = self.font.render(self.text, 1, self.font_color)
        pos = self.font_pos or [(self.rect.width - font.get_rect().width)//2,
                                (self.rect.height - font.get_rect().height)//2]
        self.image.blit(font, pos)
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def _onclick(self):
        self.onclick()

    def update(self, events):
        if self.rect.collidepoint(*get_mouse_pos()) and get_mouse_pressed()[0]:
            self.image.fill(self.background_color_click)
        elif self.rect.collidepoint(*get_mouse_pos()):
            self.image.fill(self.background_color_cover)
            for event in events:
                if event.type == MOUSEBUTTONUP:
                    self._onclick()
        else:
            self.image.fill(self.background_color)
