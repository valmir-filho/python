"""
The input is a string str of digits. Cut the string into chunks
(a chunk here is a substring of the initial string) of size sz
(ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk;
otherwise rotate it to the left by one position.
Put together these modified chunks and return the result as a string.

If:
- sz is <= 0 or if str == "" return ""
- sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return.
"""


def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""

    result = []
    for i in range(0, len(strng), sz):
        chunk = strng[i:i+sz]
        if len(chunk) == sz:
            # Check if the sum of digits is divisible by 2.
            digit_sum = sum(int(digit) for digit in chunk)
            if digit_sum % 2 == 0:
                # Reverse the chunk.
                result.append(chunk[::-1])
            else:
                # Rotate the chunk to the left by one position.
                result.append(chunk[1:] + chunk[0])
    
    return ''.join(result)
