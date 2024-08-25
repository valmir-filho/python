"""
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.
"""


def nb_dig(n, d):
    # Convert d to string for easier comparison.
    d_str = str(d)
    count = 0

    # Iterate through each number from 0 to n.
    for i in range(n + 1):
        # Square the number.
        square = i * i
        # Convert the square to string.
        square_str = str(square)
        # Count occurrences of d_str in the square_str.
        count += square_str.count(d_str)
    
    return count
