"""
The Story
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents.
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space
left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview
You have to write a function that accepts three parameters:
- Cap is the amount of people the bus can hold excluding the driver.
- On is the number of people on the bus excluding the driver.
- Wait is the number of people waiting to get on to the bus excluding the driver.

If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
"""


def enough(cap, on, wait):
    # Calculate the available space on the bus.
    available_space = cap - on
    # If the available space is greater than or equal to the waiting passengers.
    if available_space >= wait:
        return 0
    else:
        # Calculate the number of passengers who cannot fit.
        return wait - available_space
