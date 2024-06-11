"""
Write a function named get_planet_name that takes an integer id as its parameter.
The function should return the name of the planet corresponding to the given id.
"""


def get_planet_name(id):
    planet_names = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planet_names.get(id, "")
