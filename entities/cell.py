import pygame

class Cell:
    def __init__(self, row, col, x, y, size, id):
        self.row = row
        self.col = col
        self.id = id
        self.rect = pygame.Rect(x, y, size, size)
        self.selected = False
        self.base_color = (90, 180, 255)
        self.pressed_color = (255, 180, 90)
        self.target_color = (0, 255, 0)
        self.is_target = False
        self.current_color = self.base_color


    def draw(self, surface):
        pygame.draw.rect(surface, self.current_color, self.rect)

    def press(self):
        self.current_color = self.pressed_color
        if self.is_target:
            return True
        return False

    def release(self):
        self.current_color = self.base_color
        self.is_target = False

    def set_target(self):
        self.is_target = True
        self.current_color = self.target_color