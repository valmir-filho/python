""
In this little assignment you are given a string of
space separated numbers, and have to return the highest
and lowest number.
"""


def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    return f"{max(num_list)} {min(num_list)}"
