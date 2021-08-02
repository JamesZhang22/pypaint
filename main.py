from typing import Tuple, List
from utils import *
import sys

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyPaint")
icon = pygame.image.load('images\paintbrush.png')
pygame.display.set_icon(icon)
pygame.mouse.set_cursor(*pygame.cursors.diamond)

def get_grid(rows: int, cols: int, color: Tuple) -> List:
    grid = []

    for row in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[row].append(color)

    return grid


def draw_grid(screen: pygame.Surface, grid: List, grid_lines: bool, rows: int, cols: int) -> None:
    pixel_size = WIDTH // cols
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(screen, pixel, (j * pixel_size, i * pixel_size, pixel_size, pixel_size))

    if grid_lines:
        for i in range(rows + 1):
            pygame.draw.line(screen, BLACK, (0, i * pixel_size), (WIDTH, i * pixel_size))

        for j in range(cols + 1):
            pygame.draw.line(screen, BLACK, (j * pixel_size, 0), (j * pixel_size, HEIGHT - TOOLBAR_HEIGHT))


def draw_main(screen: pygame.Surface, grid: List, buttons: List, lines: bool, rows: int, cols: int) -> None:
    screen.fill(BG_COLOR)
    draw_grid(screen, grid, lines, rows, cols)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()


def draw_settings(screen: pygame.Surface, buttons: List) -> None:
    screen.fill(GRAY)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()


def get_row_col_from_pos(pos: Tuple, rows: int, cols: int) -> Tuple:
    pixel_size = WIDTH // cols
    x, y = pos
    col = x // pixel_size
    row = y // pixel_size

    if row >= rows:
        raise IndexError

    return row, col


def main(rows: int, cols: int, grid_lines: bool, grid = None) -> None:
    running = True
    clock = pygame.time.Clock()
    if not grid:
        grid = get_grid(rows, cols, BG_COLOR)
    drawing_color = BLACK

    button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
    buttons = [
        Buttons(15, button_y, 50, 50, BLACK, 1),
        Buttons(75, button_y, 50, 50, RED, 1),
        Buttons(135, button_y, 50, 50, GREEN, 1),
        Buttons(195, button_y, 50, 50, BLUE, 1),
        Buttons(255, button_y, 50, 50, WHITE, 1, None, BLACK, "images\paint-palette.png"),
        Buttons(315, button_y, 50, 50, WHITE, 1, None, BLACK, "images\eraser-tool.png"),
        Buttons(375, button_y, 50, 50, WHITE, 1, None, BLACK, "images\paint-bucket.png"),
        Buttons(435, button_y, 50, 50, WHITE, 1, None, BLACK, "images\setting.png"),
        Buttons(50, button_y - 15, 400, 5, BLACK, 1, None, BLACK)
    ]

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                try:
                    row, col = get_row_col_from_pos(pos, rows, cols)
                    grid[row][col] = drawing_color
                    # print(grid)
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
                            grid = get_grid(rows, cols, drawing_color)
                        elif button.x == 435:
                            settings(rows, cols, grid_lines, grid)
                        buttons[8].color = buttons[8].text_color = drawing_color
                        
        draw_main(SCREEN, grid, buttons, grid_lines, rows, cols)


def settings(rows: int, cols: int, grid_lines: bool, grid: List) -> None:
    running = True
    clock = pygame.time.Clock()
    settings_buttons = [
        Buttons(450, 20, 30, 30, GRAY, 1, None, BLACK, "images\close.png"),
        Buttons(165, 20, 170, 40, GRAY, 34, "Settings", BLACK),
        Buttons(30, 100, 80, 40, GRAY, 24, "Size:", BLACK),
        Buttons(160, 100, 50, 40, GRAY, 24, "10", BLACK),
        Buttons(260, 100, 50, 40, GRAY, 24, "50", BLACK),
        Buttons(360, 100, 50, 40, GRAY, 24, "100", BLACK),
        Buttons(30, 180, 80, 40, GRAY, 24, "Grid:", BLACK),
        Buttons(190, 180, 70, 40, GRAY, 24, "On", BLACK),
        Buttons(260, 180, 70, 40, GRAY, 24, "Off", BLACK),
        Buttons(200, 260, 80, 40, GRAY, 24, "Save", BLACK),
        Buttons(200, 340, 80, 40, GRAY, 24, "Load", BLACK)
    ]
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                for button in settings_buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "10":
                        main(10, 10, grid_lines)
                    elif button.text == "50":
                        main(50, 50, grid_lines)
                    elif button.text == "100":
                        main(100, 100, grid_lines)
                    elif button.text == "On":
                        main(rows, cols, True)
                    elif button.text == "Off":
                        main(rows, cols, False)
                    elif button.text == "Save":
                        save(grid)
                    elif button.text == "Load":
                        img = load("pypaint.png")
                        main(img[0], img[0], True, img[1])
                    elif button.x == 450:
                        running = False

        draw_settings(SCREEN, settings_buttons)


if __name__ == "__main__":
    main(ROWS, COLS, DRAW_GRID_LINES)