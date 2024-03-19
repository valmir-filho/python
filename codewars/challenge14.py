"""
Create a method to see whether the string is ALL CAPS.

Examples (Input -> Output):
1) "c" -> False.
2) "C" -> True.
3) "hello I AM DONALD" -> False.
4) "HELLO I AM DONALD" -> True.
5) "ACSKLDFJSgSKLDFJSKLDFJ" -> False.
6) "ACSKLDFJSGSKLDFJSKLDFJ" -> True.
"""


def is_all_caps(s: str) -> bool:
    # Check if the string is the same as its uppercase version.
    return s == s.upper()

# Usage example.
test_strings = ["c", "C", "hello I AM DONALD", "HELLO I AM DONALD", "ACSKLDFJSgSKLDFJSKLDFJ", "ACSKLDFJSGSKLDFJSKLDFJ"]
results = [is_all_caps(s) for s in test_strings]

for test_string, result in zip(test_strings, results):
    print(f'"{test_string}" -> {result}')
