"""
XOR is everywhere in crypto. It's simple, reversible, and shows up constantly in CTF challenges.
It is a bitwise eXclusive OR (or XOR) operation turning plaintext into cipher text.
Its key feature is that reapplying the exact same XOR operation with the same key instantly decrypts the data back to its original form.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

The idea: Take each character in your message and XOR it with a character from the key (use ASCII encoding). If the key is shorter than the message, just loop it.

The cool part? XOR the result with the same key again and you get the original message back (done byte by byte).

cipher_text = data ^ key
data = cipher_text ^ key

Write xor_cipher(text, key) that does exactly this.

xor_cipher("HELLO", "KEY")  # some encrypted gibberish.
xor_cipher(xor_cipher("HELLO", "KEY"), "KEY")  # "HELLO" again.

Both inputs are non-empty strings. Characters can be any ASCII value.
"""


def xor_cipher(text, key):
    result = []
    
    for i, char in enumerate(text):
        text_ord = ord(char)
        key_ord = ord(key[i % len(key)])
        
        xored = text_ord ^ key_ord
        result.append(chr(xored))
    
    return ''.join(result)
