"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

- find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2;
- find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55.

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr):
    # If the first two numbers are the same, the unique number is not among them.
    if arr[0] == arr[1]:
        common = arr[0]
    else:
        # If the first two numbers are different, the unique number must be one of them.
        return arr[0] if arr[0] != arr[2] else arr[1]
    
    # Loop through the array to find the number that is different from the common one.
    for num in arr:
        if num != common:
            return num
