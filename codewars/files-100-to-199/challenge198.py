"""
Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does,
he wants to know how many years 'Y' this sum 'P' has to be kept in the bank
in order for it to amount to a desired sum of money 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly.
After paying taxes 'T' for the year the new sum is re-invested.

Note to Tax: not the invested principal is taxed, but only the year's accrued interest
"""


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        # Calculate the interest for the current year.
        yearly_interest = principal * interest
        # Calculate the taxed interest.
        net_interest = yearly_interest * (1 - tax)
        # Update the principal with the net interest.
        principal += net_interest
        # Increment the year count.
        years += 1
    return years
