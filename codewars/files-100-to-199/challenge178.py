"""
Define a method hello that returns "Hello, Name!" to a given name,
or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).
"""


def hello(name=""):
    # Check if the name is not provided or is an empty string.
    if not name:
        return "Hello, World!"
    else:
        # Capitalize the first letter and make the rest lowercase.
        return f"Hello, {name.capitalize()}!"
