"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd".
Your task is to process a string with "#" symbols.
"""


def clean_string(s):
    stack = []
    for char in s:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
