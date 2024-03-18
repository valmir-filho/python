"""
Create a method to see whether the string is ALL CAPS.

Examples (input -> output).
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
"""


def is_all_caps(s: str) -> bool:
    # Check if the string is the same as its uppercase version.
    return s == s.upper()

# Test the function with the provided examples.
test_strings = ["c", "C", "hello I AM DONALD", "HELLO I AM DONALD", "ACSKLDFJSgSKLDFJSKLDFJ", "ACSKLDFJSGSKLDFJSKLDFJ"]
results = [is_all_caps(s) for s in test_strings]

for test_string, result in zip(test_strings, results):
    print(f'"{test_string}" -> {result}')
