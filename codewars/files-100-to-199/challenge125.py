"""
"Pits" and "lands" are physical features on the surface of a CD that represent binary data.
Pits are small depressions or grooves on the surface of the CD, while lands are flat areas between two adjacent pits.
The pits and lands themselves do not directly represent the zeros and ones of binary data.
Instead, Non-return-to-zero, inverted encoding is used: a change from pit to land or land to pit indicates a one,
while no change indicates a zero.
In this Kata, you should implement a function, that takes integer in range [0..255] (8 bits), and returns combination
of pits and lands that encode the number. Result should have format of string: PLLPL... where P represents pit and L represents land.
Combination should always start with pit. Numbers should be encoded in little-endian, which means you start from least significant bit.
"""


def encode_cd(n):
    if not (0 <= n <= 255):
        raise ValueError("Input must be within the range 0..255")
    
    binary_rep = format(n, '08b')[::-1]
    result = ['P']
    
    for bit in binary_rep:
        if bit == '1':
            if result[-1] == 'P':
                result.append('L')
            else:
                result.append('P')
        else:
            result.append(result[-1])
    
    return ''.join(result)
