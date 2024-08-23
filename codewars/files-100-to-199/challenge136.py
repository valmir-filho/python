"""
Implement a pseudo-encryption algorithm which given a string S and an integer N
concatenates all the odd-indexed characters of S with all the even-indexed characters of S,
this process should be repeated N times.
"""


def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        odd_chars = ''.join([text[i] for i in range(1, len(text), 2)])
        even_chars = ''.join([text[i] for i in range(0, len(text), 2)])
        text = odd_chars + even_chars

    return text


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    half_len = len(encrypted_text) // 2
    for _ in range(n):
        odd_chars = encrypted_text[:half_len]
        even_chars = encrypted_text[half_len:]
        text = ''.join(even_chars[i:i+1] + odd_chars[i:i+1] for i in range(half_len + 1))

        encrypted_text = text[:len(encrypted_text)]

    return encrypted_text
