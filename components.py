import pygame
from math import sqrt


class Window:
    def __init__(self, title: str):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(title)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()


class Circle:
    def __init__(self, x: int, y: int, radius: int, colour: tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self, window: Window):
        pygame.draw.circle(window.screen, self.colour, (self.x, self.y), self.radius)

    def distance_to(self, x: int, y: int, radius: int):
        return sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def circle_lies_within(self, x: int, y: int, radius: int):
        return self.radius > self.distance_to(x, y, radius) + radius
