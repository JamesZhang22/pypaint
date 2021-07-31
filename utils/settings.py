import pygame
from typing import Tuple

pygame.init()
pygame.font.init()

# Colors
BLACK = (0, 0, 0)
GRAY = (199, 199, 199)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Frames per second
FPS = 60

# Dimensions
WIDTH = 500
HEIGHT = 600

# Pixels
ROWS = 50
COLS = 50

# Toolbar
TOOLBAR_HEIGHT = HEIGHT - WIDTH

# Pixels
PIXEL_SIZE = WIDTH // COLS

# Background Color
BG_COLOR = WHITE

# Grid lines
DRAW_GRID_LINES = True

def get_font(size: int):
    return pygame.font.SysFont("monospace", size)