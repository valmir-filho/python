"""
How sexy is your name? Write a program that calculates how sexy one's name is according to the criteria below.

There is a preloaded dictionary of letter scores called SCORES(Python & JavaScript) / $SCORES (Ruby).
Add up the letters (case-insensitive) in your name to get your sexy score. Ignore other characters.

SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3, 'H': 10, 'I': 200, 'J': 100,
          'K': 114, 'L': 100, 'M': 25, 'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

The program must return how sexy one's name is according to the "Sexy score ranking" chart.

score <= 60: 'NOT TOO SEXY'
61 <= score <= 300: 'PRETTY SEXY'
301 <= score <= 599: 'VERY SEXY'
score >= 600: 'THE ULTIMATE SEXIEST'
"""


def sexy_name(name):
    """
    Calculates a name's "sexy score" and returns a ranking based on the score.

    Args:
        name (str): The name to be scored.

    Returns:
        str: The sexy score ranking.
    """
    SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
              'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
              'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
              'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

    score = 0
    
    # Iterate through each character in the name.
    for char in name:
        # Convert the character to uppercase to match the keys in the SCORES dictionary.
        upper_char = char.upper()
        # Add the score of the character if it exists in the dictionary.
        if upper_char in SCORES:
            score += SCORES[upper_char]

    # Determine the ranking based on the calculated score.
    if score <= 60:
        return 'NOT TOO SEXY'
    elif 61 <= score <= 300:
        return 'PRETTY SEXY'
    elif 301 <= score <= 599:
        return 'VERY SEXY'
    else:  # score >= 600.
        return 'THE ULTIMATE SEXIEST'
