from random import random
from math import cos, sin
from components import Window, Circle


class Cans:
    def __init__(self, ring: Circle, starting_ring: Circle, can_radius: int, total: int, min_dist: int, colour: tuple):
        self.max_x = ring.x + ring.radius - can_radius
        self.max_y = ring.y + ring.radius - can_radius
        self.min_dist = min_dist + (can_radius * 2)
        self.can_radius = can_radius
        self.cans = self.get_random_can_layout(total, colour, ring, starting_ring)

    def get_random_position_in_ring(self, ring: Circle, starting_ring: Circle):
        inner_radius = starting_ring.radius + self.can_radius
        outer_radius = ring.radius - self.can_radius
        radius = (random() * (outer_radius - inner_radius)) + inner_radius
        angle = random() * 360
        x = int(radius * cos(angle)) + ring.x
        y = int(radius * sin(angle)) + ring.y
        return x, y

    def get_random_can_layout(self, total: int, colour: tuple, ring: Circle, starting_ring: Circle):
        cans = []
        attempts = 0
        while len(cans) < total:
            valid = False
            while (not valid):
                x, y = self.get_random_position_in_ring(ring, starting_ring)
                valid = True
                attempts += 1
                for can in cans:
                    if can.distance_to(x, y, self.can_radius) < self.min_dist:
                        valid = False
                        break

            if valid:
                cans.append(Circle(x, y, self.can_radius, colour))

        print(f"Attempted {attempts} configurations")
        return cans

    def draw(self, window: Window):
        for can in self.cans:
            can.draw(window)
