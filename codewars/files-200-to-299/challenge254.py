"""
The code provided is supposed replace all the dots in the specified String str with dashes, but it's not working properly.
Fix the bug so we can all go home early.
String str will never be null.
"""

import re


def replace_dots(s):
    return re.sub(r"\.", "-", s)
