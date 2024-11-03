"""
Write the function sharePrice() that calculates,
and returns the current price of your share,
given the following two arguments:

- invested(number), the amount of money you initially invested in the given share;
- changes(array of numbers), contains your shares daily movement percentages.

The returned number, should be in string format,
and it's precision should be fixed at 2 decimal numbers.
"""


def share_price(invested, changes):
    # Start with the initial investment as the current price.
    current_price = invested
    
    # Update the current price based on percentage changes.
    for change in changes:
        current_price *= (1 + change / 100)
    
    # Format the result to two decimal places and return as a string.
    return f"{current_price:.2f}"
