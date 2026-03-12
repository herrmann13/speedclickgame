import pygame
import random  # main.py (topo)
from entities.cell import Cell
from entities.scoreboard import Scoreboard

pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ROWS, COLS = 8, 12
CELL_SIZE = 80
MARGIN = 2

grid_w = COLS * CELL_SIZE
grid_h = ROWS * CELL_SIZE
offset_x = (WIDTH - grid_w) // 2
offset_y = (HEIGHT - grid_h) // 2

cells = []
id_count = 0

for r in range(ROWS):
    row_cells = []
    for c in range(COLS):
        id_count += 1
        x = offset_x + c * CELL_SIZE + MARGIN
        y = offset_y + r * CELL_SIZE + MARGIN
        size = CELL_SIZE - 2 * MARGIN
        row_cells.append(Cell(r, c, x, y, size, id_count))
    cells.append(row_cells)


TARGET_EVENT = pygame.USEREVENT + 1
TARGET_INTERVAL_MS = 1000
pygame.time.set_timer(TARGET_EVENT, TARGET_INTERVAL_MS)
all_cells = [cell for row in cells for cell in row]
current_target = random.choice(all_cells)
current_target.set_target()

scoreboard = Scoreboard()
pressed_cell = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == TARGET_EVENT:
            current_target.is_target = False
            current_target.current_color = current_target.base_color
            current_target = random.choice(all_cells)
            current_target.set_target()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for row in cells:
                for cell in row:
                    if cell.rect.collidepoint(mouse_pos):
                        pressed_cell = cell
                        if pressed_cell.press():
                            scoreboard.add_points(1)
                        break
                    
                if pressed_cell:
                    break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if pressed_cell:
                pressed_cell.release()
                pressed_cell = None

    screen.fill((25, 25, 25))

    scoreboard.render(screen)

    for row in cells:
        for cell in row:
            cell.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()