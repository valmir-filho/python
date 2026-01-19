"""
Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)
"""


def reverse(lst):
    empty_list = list()  # use this!
    while len(lst) > 0:
        empty_list.append(lst.pop())
    return empty_list
