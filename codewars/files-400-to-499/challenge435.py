"""
"Riley, I don't need that anymore, I need to know how many!"

This kata is a continuation of Keypad Heist: The Riley Poole Logic. It is recommended to solve that kata first.

In the previous mission, you helped Riley generate all possible passwords.
But the FBI has upgraded their security. Now, the keypads are larger, and the passwords are much longer.

Riley’s laptop keeps crashing because there are quadrillions of combinations.
He doesn't need to see the passwords anymore; he just needs to know the total
number of unique combinations so he can estimate how many years it will take to brute-force it.

The Mission

Create a function count_passwords(keys_count, length) that returns the number of unique strings of a specific length
that can be formed using exactly keys_count unique characters, ensuring each character is used at least once.

Example

count_passwords(2, 3) 
# Imagine keys are 'a' and 'b'. 
# Valid: "aab", "aba", "abb", "baa", "bab", "bba"
# Result: 6
"""

from math import comb


def count_passwords(keys_count, length):
    if keys_count == 0:
        return 1 if length == 0 else 0
    
    if keys_count > length:
        return 0
    
    total = 0
    for i in range(keys_count + 1):
        total += (-1) ** i * comb(keys_count, i) * (keys_count - i) ** length
    
    return total
