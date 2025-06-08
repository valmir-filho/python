""
Given three arrays of integers, return the sum of elements that are common in all three arrays.
"""

# The logic for the 'common' function.
from collections import Counter


def common(a, b, c):
    # Step 1: Create frequency maps for each array.
    # The Counter class is a specialized dictionary for this purpose.
    count_a = Counter(a)
    count_b = Counter(b)
    count_c = Counter(c)
    
    total_sum = 0
    
    # Step 2: Iterate through the unique elements of the first array.
    for number, count_in_a in count_a.items():
        # Step 3: Check if the element is common to all three.
        if number in count_b and number in count_c:
            # Find the minimum number of occurrences across all three arrays.
            min_count = min(count_in_a, count_b[number], count_c[number])
            
            # Add the element's value, repeated by its common count, to the sum.
            total_sum += number * min_count
            
    return total_sum
