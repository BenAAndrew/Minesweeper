import configparser

from components import Window, Circle
from cans import Cans


def to_int_array(string):
    return [int(i) for i in string.split(",")]


config = configparser.ConfigParser()
config.read("config.ini")

SCREEN = config["Screen"]
RING = config["Ring"]
WIDTH, HEIGHT = to_int_array(SCREEN["DIMENSIONS"])

# Define rings
ring_radius = int(min(WIDTH, HEIGHT) / 2)
ring = Circle(int(WIDTH / 2), int(HEIGHT / 2), ring_radius, to_int_array(RING["COLOUR"]))

starting_ring_radius = int(float(RING["STARTING_RING_SIZE_PERCENTAGE"]) * ring_radius)
starting_ring = Circle(
    int(WIDTH / 2), int(HEIGHT / 2), starting_ring_radius, to_int_array(RING["STARTING_RING_COLOUR"])
)

# Generate cans
cans = Cans(
    ring,
    starting_ring,
    int(float(RING["CAN_SIZE_PERCENTAGE"]) * ring_radius),
    int(RING["CANS"]),
    int(float(RING["MIN_DIST_PERCENTAGE_BETWEEN_CANS"]) * ring_radius),
    to_int_array(RING["CAN_COLOUR"]),
)

# Define screen
screen = Window(SCREEN["TITLE"])

while True:
    screen.update()
    ring.draw(screen)
    starting_ring.draw(screen)
    cans.draw(screen)
