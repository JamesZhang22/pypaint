from pygame import font
from .settings import *

class Buttons:
    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple, font_size: int, text=None, text_color=BLACK, image=None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font_size = font_size
        self.text = text
        self.text_color = text_color
        self.image = image


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.text_color, (self.x, self.y, self.width, self.height), 2)

        if self.text:
            myfont = get_font(self.font_size)
            text_surface = myfont.render(self.text, True, self.text_color)
            screen.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, self.y + self.height / 2 - text_surface.get_height() / 2))
        if self.image:
            self.image_load = pygame.image.load(self.image)
            screen.blit(self.image_load, (self.x + (self.width - self.image_load.get_width()) / 2, self.y + (self.height - self.image_load.get_height()) / 2))


    def clicked(self, pos: Tuple) -> bool:
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        
        return True