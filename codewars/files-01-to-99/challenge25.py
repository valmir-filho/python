"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""


def break_camel_case(s):
  return ''.join(' ' + c if c.isupper() and i != 0 else c for i, c in enumerate(s))

# Usage example.
test_string = "exampleCamelCase."
print(break_camel_case(test_string))
