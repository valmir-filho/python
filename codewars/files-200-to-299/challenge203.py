""
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process.

Example:

arr = [1,-2,3,4,-5,-4,3,2,1]
range = [[1,3],[0,4],[6,8]]
should return 6
 
Calculation process:

range[1,3] = arr[1]+arr[2]+arr[3] = 5
range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
range[6,8] = arr[6]+arr[7]+arr[8] = 6

So the maximum sum value is 6.

Note:

arr/$a always has at least 5 elements;
range/$range/ranges always has at least 1 element;
All inputs are valid.
"""


def max_sum(arr, ranges):
    max_value = float('-inf')  # Start with the smallest possible value.
    for start, end in ranges:
        range_sum = sum(arr[start:end+1])  # Sum elements within the range [start, end].
        max_value = max(max_value, range_sum)  # Update max_value if the new sum is larger.
    return max_value
