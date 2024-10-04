"""
Implement the function generateRange which takes three arguments (start, stop, step)
and returns the range of integers from start to stop (inclusive) in increments of step.
"""


def generate_range(start, stop, step):
    return list(range(start, stop + 1, step))
