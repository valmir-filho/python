"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0);
d decrements the value;
s squares the value;
o outputs the value into the return array.

Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""


def parse(data):
    value = 0  # Initial value.
    result = []  # List to store output values.

    for char in data:
        if char == 'i':
            value += 1  # Increment.
        elif char == 'd':
            value -= 1  # Decrement.
        elif char == 's':
            value = value ** 2  # Square the value.
        elif char == 'o':
            result.append(value)  # Output the value to the result list.

    return result
