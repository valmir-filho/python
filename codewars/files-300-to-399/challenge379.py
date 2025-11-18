"""
You'll be passed an array of objects (list) - you must sort them in descending order based on the value of the specified property (sortBy).
"""


def sort_list(sort_by, lst):
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)
