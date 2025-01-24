"""
Consider a sequence u where u is defined as follows: The number u(0) = 1 is the first one in u.

For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.

There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...].

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example: dbl_linear(10) should return 22.

Note: Focus attention on efficiency.
"""

import heapq


def dbl_linear(n):
    # Initialize the heap with the first element.
    heap = [1]
    seen = {1}  # To track numbers already in the sequence.

    for _ in range(n):
        # Pop the smallest element from the heap.
        current = heapq.heappop(heap)
        
        # Generate the next two numbers and add them to the heap if not already present.
        y = 2 * current + 1
        z = 3 * current + 1
        
        if y not in seen:
            heapq.heappush(heap, y)
            seen.add(y)
        
        if z not in seen:
            heapq.heappush(heap, z)
            seen.add(z)
    
    # The n-th number will now be at the top of the heap.
    return heapq.heappop(heap)
