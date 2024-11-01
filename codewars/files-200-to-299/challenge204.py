"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.
"""


def capitalize(s):
    even_caps = ''.join([c.upper() if i % 2 == 0 else c for i, c in enumerate(s)])
    odd_caps = ''.join([c.upper() if i % 2 != 0 else c for i, c in enumerate(s)])
    return [even_caps, odd_caps]
