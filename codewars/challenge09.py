"""
There is a bus moving in the city which takes and drops some people at each bus stop. You are provided with a list (or array) of
integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people
that get off the bus (the second item) at a bus stop. Your task is to return the number of people who are still on the bus after
the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might
still be inside the bus, they are probably sleeping there :D.

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't
be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.
"""


def number_of_people_on_bus(bus_stops):
    # Initialize the number of people on the bus.
    people_on_bus = 0
    
    # Iterate through each bus stop.
    for on, off in bus_stops:
        # Add people getting on and subtract people getting off.
        people_on_bus += on - off
    
    # Return the final count of people on the bus.
    return people_on_bus

# Usage example.
bus_stops = [(10, 0), (3, 5), (5, 8)]
print(number_of_people_on_bus(bus_stops))
