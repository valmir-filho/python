"""
Your task is to sum the differences between consecutive pairs in the array in descending order.
"""


def sum_of_differences(arr):
    if not arr or len(arr) <= 1:
        return 0
    
    arr.sort(reverse=True)
    
    total_sum = 0
    for i in range(len(arr) - 1):
        total_sum += arr[i] - arr[i+1]
        
    return total_sum
