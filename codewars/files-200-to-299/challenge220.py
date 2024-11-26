"""
Create a method that takes as input a name, city,
and state to welcome a person. Note that name will
be an array consisting of one or more values that
should be joined together with one space between each,
and the length of the name array in test cases will vary.
"""


def say_hello(name, city, state):
    # Join the name array into a single string with a space between each value.
    full_name = ' '.join(name)
    # Construct the welcome message.
    return f"Hello, {full_name}! Welcome to {city}, {state}!"
