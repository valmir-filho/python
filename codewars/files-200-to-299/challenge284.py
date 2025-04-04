"""
Task

Create a function that given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases.
In the event that an element appears more than once in the input sequence, only one of them will be taken into account for the result, discarding the rest.

Input

Sequence of strings. Valid characters for those strings are uppercase and lowercase characters from the alphabet and whitespaces.

Output

Sequence of elements. Each element is the group of inputs that can be obtained by rotating the strings.
Sort the elements of each group alphabetically.
Sort the groups descendingly by size and in the case of a tie, by the first element of the group alphabetically.
"""


def group_cities(seq):
    seen = set()
    groups = {}

    for city in seq:
        norm_city = city.lower()
        if norm_city in seen:
            continue
        seen.add(norm_city)

        # Generate all rotations.
        rotations = {norm_city[i:] + norm_city[:i] for i in range(len(norm_city))}

        # Use the sorted lowercase rotation as a key.
        found_key = None
        for key in groups:
            if key in rotations:
                found_key = key
                break

        if found_key:
            groups[found_key].add(city)
        else:
            groups[norm_city] = {city}

    # Convert sets to sorted lists.
    result = [sorted(list(group)) for group in groups.values()]
    
    # Sort by size descending, then alphabetically.
    result.sort(key=lambda x: (-len(x), x[0].lower()))
    return result
