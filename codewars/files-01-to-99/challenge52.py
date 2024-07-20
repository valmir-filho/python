"""
There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required
for all the customers to check out!

Input
- customers: an array of positive integers representing the queue.
Each integer represents a customer, and its value is the amount of
time they require to check out.
- n: a positive integer, the number of checkout tills.

Output
- The function should return an integer, the total time required.
"""


def queue_time(customers, n):
    # Create a list of tills with initial checkout time 0.
    tills = [0] * n
    # Iterate through each customer.
    for time in customers:
        # Find the till with the shortest checkout time.
        min_till = min(tills)
        # Add the current customer's time to that till.
        tills[tills.index(min_till)] += time
    # Return the maximum checkout time among all tills.
    return max(tills)
