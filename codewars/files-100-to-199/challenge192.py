"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35.
four(plus(nine())) # must return 13.
eight(minus(three())) # must return 5.
six(divided_by(two())) # must return 3.

Requirements:

- There must be a function for each number from 0 ("zero") to 9 ("nine").
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by.
- Each calculation consist of exactly one operation and two numbers.
- The most outer function represents the left operand, the most inner function represents the right operand.
- Division should be integer division.
"""


def zero(operation=None): 
    return 0 if operation is None else operation(0)


def one(operation=None): 
    return 1 if operation is None else operation(1)


def two(operation=None): 
    return 2 if operation is None else operation(2)


def three(operation=None): 
    return 3 if operation is None else operation(3)


def four(operation=None): 
    return 4 if operation is None else operation(4)


def five(operation=None): 
    return 5 if operation is None else operation(5)


def six(operation=None): 
    return 6 if operation is None else operation(6)


def seven(operation=None): 
    return 7 if operation is None else operation(7)


def eight(operation=None): 
    return 8 if operation is None else operation(8)


def nine(operation=None): 
    return 9 if operation is None else operation(9)


def plus(right):
    return lambda left: left + right


def minus(right):
    return lambda left: left - right


def times(right):
    return lambda left: left * right


def divided_by(right):
    return lambda left: left // right
