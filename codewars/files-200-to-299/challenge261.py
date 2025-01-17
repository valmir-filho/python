"""
Acknowledgments: I thank yvonne-liu for the idea and for the example tests :)

Description:

Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

- Your message is a string containing space separated words;

- You need to encrypt each word in the message using the following rules:

  - The first letter must be converted to its ASCII code;
  - The second letter must be switched with the last letter.

- Keepin' it simple: There are no special characters in the input.
"""


def encrypt_this(text):
    # Split the text into words.
    words = text.split()
    encrypted_words = []

    for word in words:
        # Convert the first letter to its ASCII code.
        ascii_code = str(ord(word[0]))

        if len(word) == 1:
            # If the word has only one letter, use only the ASCII code.
            encrypted_word = ascii_code
        elif len(word) == 2:
            # If the word has two letters, just add the second letter.
            encrypted_word = ascii_code + word[1]
        else:
            # For words with more than two letters, swap the second and last letters.
            encrypted_word = ascii_code + word[-1] + word[2:-1] + word[1]

        # Append the encrypted word to the list.
        encrypted_words.append(encrypted_word)

    # Join the encrypted words with spaces and return.
    return ' '.join(encrypted_words)
