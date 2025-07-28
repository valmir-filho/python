"""
Given a mixed array of number and string representations of integers,
add up the non-string integers and subtract the total of the string integers.
Return as a number.
"""


def div_con(x):
    total_non_string_integers = 0
    total_string_integers = 0

    for item in x:
        if isinstance(item, int):
            total_non_string_integers += item
        elif isinstance(item, str):
            # Attempt to convert string to integer, assuming valid integer representation.
            try:
                total_string_integers += int(item)
            except ValueError:
                # Handle cases where a string might not be a valid integer representation.
                # For this problem, we assume all strings are valid integer representations.
                # If not, you might want to log this or raise an error.
                pass 
    
    return total_non_string_integers - total_string_integers
