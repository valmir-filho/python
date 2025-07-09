"""
Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function accepting 3 arguments (in order):

- left - The current floor of the left elevator;
- right - The current floor of the right elevator;
- call - The floor that called an elevator.

It should return the name of the elevator closest to the called floor ("left"/"right").
In the case where both elevators are equally distant from the called floor, choose the elevator to the right.
You can assume that the inputs will always be valid integers between 0-2.
"""


def elevator(left, right, call):
    # Calculate the absolute difference between the left elevator's current floor and the call floor.
    left_diff = abs(left - call)
    # Calculate the absolute difference between the right elevator's current floor and the call floor.
    right_diff = abs(right - call)

    # If the left elevator is closer, return "left".
    if left_diff < right_diff:
        return "left"
    # If the right elevator is closer or they are equidistant, return "right".
    else:
        return "right"
    
