"""
Oh no! The planets are jumbled up and they have lost their moons!

TASK

Given two lists, the planets and the moons, you have to return a two-dimensional list with the planets and their respective moons.

The dictionary with the planets' names (in the correct order) as the keys and their iconic moons' names as the values is given preloaded with the name planet_moons:

planet_moons = {
    'Mercury': [],
    'Venus': [],
    'Earth': ['Moon'],
    'Mars': ['Deimos', 'Phobos'],
    'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
    'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
    'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
    'Neptune': ['Nereid', 'Proteus', 'Triton']
}

The names of all the moons are sorted.

Mercury and Venus have no moons at all.

The moons list will have random assorted moons. The planets list will have some (or all) planets, in any order.

What you return should have a list for each planet with the moons you found for it.
The planets should be ordered as per the order in the planet_moons dictionary,
which is ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].

If a moon is present but its planet is not, ignore it.

The moons for each planet should be sorted and are then swept up by the planet on alternative sides. The first moon goes on the right of the planet, the next one on the left, and so on.

For example, if "Saturn" is given in the planets, and the moons are ["Rhea", "Tethys", "Iapetus", "Dione"],
the first moon (after sorting), "Dione", is put on the right. The next moon, "Iapetus", now goes to the left of "Saturn".
"Rhea" this time has to go to the right of "Saturn". Last, "Tethys" goes to the left, because the moons have to be placed alternatively.
So "Saturn"'s orbit after collecting its lost planets would look like ["Tethys", "Iapetus", "Saturn", "Dione", "Rhea"].

EXAMPLE

If the planets are ["Venus", "Neptune", "Jupiter", "Earth", "Mars"] and the moons are ["Proteus", "Rhea", "Io", "Moon", "Nereid", "Triton", "Phobos"], the Solar System you return should be:

[["Venus"], ["Earth", "Moon"], ["Mars", "Phobos"], ["Jupiter", "Io"], ["Proteus", "Neptune", "Nereid", "Triton"]]

# "Venus" is alone in its orbit.
# "Earth" has its (our) "Moon" given, so it's found and put to the right.
# "Mars" finds "Phobos" and puts it to the right, but "Deimos", its other moon is not given, and remains lost.
# "Jupiter" only finds "Io" from its moons.
# "Neptune" first takes "Nereid", even though "Proteus" comes first in the list of moons, "Nereid" comes first after sorting.
# Next it puts "Proteus" to the left, and finally "Triton" again to the right.
# "Saturn" is not present in the list of planets, and so "Rhea" remains lost

NOTES

The planets list won't contain anything outside of the given planets and same applies for the moons list.
All the names in both the lists will be title-cased.

The Solar System series

1. Jumbled Planets
2. Planet Mnemonic
3. Planets on the Move
4. Meteor Shower
5. Lost Moons
"""

from preloaded import planet_moons


def lost_moons(planets, moons):
    # fast lookup: moon -> its planet.
    moon_to_planet = {}
    for p, ms in planet_moons.items():
        for m in ms:
            moon_to_planet[m] = p

    planets_set = set(planets)

    # collect only moons whose planet exists in the given planets list.
    found = {p: [] for p in planets_set}
    for m in moons:
        p = moon_to_planet.get(m)
        if p in planets_set:
            found[p].append(m)

    # build result in canonical planet order, with alternating placement (R, L, R, L...).
    result = []
    for p in planet_moons.keys():  # keeps required order
        if p not in planets_set:
            continue

        ms = sorted(found.get(p, []))

        left, right = [], []
        for i, m in enumerate(ms):
            if i % 2 == 0:   # 0th moon goes to the right.
                right.append(m)
            else:            # 1st moon goes to the left, etc.
                left.append(m)

        # moons placed to the left must appear in reverse insertion order (closest to planet last).
        orbit = left[::-1] + [p] + right
        result.append(orbit)

    return result
