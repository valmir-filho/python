"""
This series of katas will introduce you to basics of doing geometry with computers.
Point objects have attributes x and y.
Write a function calculating distance between Point a and Point b.
"""

import math


def distance_between_points(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
