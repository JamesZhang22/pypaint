from typing import Tuple, List
from utils import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyPaint")
pygame.mouse.set_cursor(*pygame.cursors.diamond)

def get_grid(rows: int, cols: int, color: Tuple) -> List:
    grid = []

    for row in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[row].append(color)

    return grid


def draw_grid(screen: pygame.Surface, grid: List) -> None:
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(screen, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(screen, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for j in range(COLS + 1):
            pygame.draw.line(screen, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_main(screen: pygame.Surface, grid: List, buttons: List) -> None:
    screen.fill(BG_COLOR)
    draw_grid(screen, grid)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()


def draw_settings(screen: pygame.Surface, buttons: List) -> None:
    screen.fill(BG_COLOR)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()


def get_row_col_from_pos(pos: Tuple) -> Tuple:
    x, y = pos
    col = x // PIXEL_SIZE
    row = y // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


running = True
clock = pygame.time.Clock()
grid = get_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [Buttons(15, button_y, 50, 50, BLACK), Buttons(75, button_y, 50, 50, RED), Buttons(135, button_y, 50, 50, GREEN), Buttons(195, button_y, 50, 50, BLUE), Buttons(255, button_y, 50, 50, WHITE, None, BLACK, "images\paint-palette.png"), Buttons(315, button_y, 50, 50, WHITE, None, BLACK, "images\eraser-tool.png"), Buttons(375, button_y, 50, 50, WHITE, None, BLACK, "images\paint-bucket.png"), Buttons(435, button_y, 50, 50, WHITE, None, BLACK, "images\setting.png"), Buttons(50, button_y - 15, 400, 5, BLACK, None, BLACK)]
settings_buttons = []

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    
                    if button.x == 15:
                        drawing_color = BLACK
                    elif button.x == 75:
                        drawing_color = RED
                    elif button.x == 135:
                        drawing_color = GREEN
                    elif button.x == 195:
                        drawing_color = BLUE
                    elif button.x == 255:
                        drawing_color = choose_color()
                    elif button.x == 315:
                        drawing_color = WHITE
                    elif button.x == 375:
                        grid = get_grid(ROWS, COLS, drawing_color)
                    elif button.x == 435:
                        print(1) # holder event
                    buttons[8].color = buttons[8].text_color = drawing_color
                    


    draw_main(SCREEN, grid, buttons)


pygame.quit()