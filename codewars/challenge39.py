"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. We want to
create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of
people that like an item.
"""


def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"
