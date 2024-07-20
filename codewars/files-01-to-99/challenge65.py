"""
Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
"""


def abbrev_name(full_name: str) -> str:
    name, surname = full_name.split()
    return f"{name[0].capitalize()}.{surname[0].capitalize()}"
