"""
A format for expressing an ordered list of integers is to use a comma separated list of either.

- individual integers;
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17";
- Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
"""


def solution(args):
    result = []
    i = 0
    
    while i < len(args):
        start = i
        
        # Find the end of the range.
        while i + 1 < len(args) and args[i + 1] == args[i] + 1:
            i += 1
        
        # Check the length of the range.
        if i - start >= 2:  # Range with at least 3 numbers.
            result.append(f"{args[start]}-{args[i]}")
        elif i - start == 1:  # Only two numbers.
            result.append(f"{args[start]}")
            result.append(f"{args[i]}")
        else:  # Single number.
            result.append(f"{args[start]}")
        
        # Move to the next number.
        i += 1

    return ",".join(result)
