import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Quantidade de linhas e colunas na grade
ROWS, COLS = 8, 12
CELL = 40
MARGIN = 2

# Tamanho da grade em pixels
grid_w = COLS * CELL
grid_h = ROWS * CELL

# Centralizar a grade na tela
offset_x = (WIDTH - grid_w) // 2
offset_y = (HEIGHT - grid_h) // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((25, 25, 25))
    for r in range(ROWS):
        for c in range(COLS):
            x = offset_x + c * CELL
            y = offset_y + r * CELL
            rect = pygame.Rect(
                x + MARGIN,
                y + MARGIN,
                CELL - 2 * MARGIN,
                CELL - 2 * MARGIN
            )
            pygame.draw.rect(screen, (90, 180, 255), rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()