import pygame


class Scoreboard:
    def __init__(self, points=0):

        self.points = points
        self.font = pygame.font.SysFont('Arial', 30)

    def render(self, surface):
        text = self.font.render(f'Score: {self.points}', True, (255, 255, 255))
        surface.blit(text, (10, 10))

    def add_points(self, amount):
        self.points += amount