import math


def turn(x, z, angle):
    first = x * math.cos(angle) - z * math.sin(angle)
    second = x * math.sin(angle) + z * math.cos(angle)
    return first, second
