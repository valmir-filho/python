"""
Complete the function to find the count of the most frequent item of an array.
You can assume that input is an array of integers. For an empty array return 0
"""

from collections import Counter


def most_frequent_item_count(collection):
    if not collection:
        return 0
    
    count = Counter(collection)
    most_frequent = count.most_common(1)[0][1]
    
    return most_frequent
