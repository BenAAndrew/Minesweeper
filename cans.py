from random import randint
from components import Window, Circle


class Cans:
    def __init__(self, ring: Circle, starting_ring: Circle, can_radius: int, total: int, min_dist: int, colour: tuple):
        self.max_x = ring.x + ring.radius - can_radius
        self.max_y = ring.y + ring.radius - can_radius
        self.min_dist = min_dist + (can_radius * 2)
        self.can_radius = can_radius
        self.cans = self.get_random_can_layout(total, colour, ring, starting_ring)

    def get_random_position_in_ring(self, ring: Circle, starting_ring: Circle):
        while True:
            x = randint(self.can_radius, self.max_x)
            y = randint(self.can_radius, self.max_y)
            in_ring = ring.circle_lies_within(x, y, self.can_radius)
            outside_starting_ring = (
                starting_ring.distance_to(x, y, self.can_radius) > starting_ring.radius + self.can_radius
            )
            if in_ring and outside_starting_ring:
                return x, y

    def get_random_can_layout(self, total: int, colour: tuple, ring: Circle, starting_ring: Circle):
        cans = []
        attempts = 0
        while len(cans) < total:
            x, y = self.get_random_position_in_ring(ring, starting_ring)

            valid = True
            for can in cans:
                if can.distance_to(x, y, self.can_radius) < self.min_dist:
                    # Clear layout and restart
                    valid = False
                    attempts += 1
                    cans = []
                    break

            if valid:
                cans.append(Circle(x, y, self.can_radius, colour))

        print(f"Attempted {attempts} configurations")
        return cans

    def draw(self, window: Window):
        for can in self.cans:
            can.draw(window)
