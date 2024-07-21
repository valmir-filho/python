"""
Story

You are working as sales person, travelling around the world, visiting your customers.
Every your jurney starts and ends in the office in London and you are not allowed to
come back to office until you visited all customers on the schedule you have got from
your boss. Your boss will give you coordinates for each cusotmer before you leave the
office. You must claim travel expences before you start jurney, fixed cost £500 for
any jurney + £10 per each mile.

Your customers may be on a ship in middle of the ocean or in middle of desert or
rainforest, in one of largest cities or smallest villages, in any country in the world.
Actually anywhere on the Earth.

Because you boss has strange sence of humour, he sometimes gives you coordinates which
does not exist on the Earth. You need to check all coordinate before you start to travel.
If you miss this catch and start your jurney, your boss will not pay any travel expences,
but worst, you will loose this kata. If you spot it before the travel, you can claim extra
fully paid holiday day and you are winning this kata.

So to summarise, there are two way to win this kata - if your boss tries to catch you and
you spot it, you are winning or if you boss gives you correct coordinates and you claim
right expences, you are winning. Otherwise you are loosing, but do not worry, you can try again.

Optimal Solution

In Optimal Solution, you will have to visit exactly 4 customers. You will need to focus on
optimal solution. With 4 customers, you have 24 options how to combine them, but your boss
will only pay the shortest / the cheapest jurney.

Nearest Neighbour Algorithm

In Nearest Neighbour Algorithm, you have have to visit between 5 and 50 customers.
You should be very familiar with validating data from your boss and calculating distance.
Unfortunately, you will not be able to use the same approach as in Optimal Solution. Even
your boss understand, that you will not be able to plan the jurney the most cost effective
way, because if you have maximum of 50 customers, you have 3.0414093 * 10^64 options to compare.
Instead, your boss expect you to use Nearest Neighbour Algorithm.
You can read more about it here: https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm.


Detailed instructions for Optinal Solution

Now, you know the story and brief description of your task.

Your office is in London, England on with these coordinates:

OFFICE = {"lat": 51.49984, "long": -0.124663}

Your boss gives you with 4 customers to visit in the following format:

[
  {"lat": 55.8642, "long": -4.2518},
  {"lat": 52.4862, "long": -1.8904},
  {"lat": 53.2268, "long": -0.5379},
  {"lat": 53.5229, "long": -1.1312}
]

Remember, all distances needs to be in miles, you needs to claim £10 per miles and fixed expence £500

To solve this kata sucessfully, please follow these steps:

1. Input Validation

Your first task is to check, if your boss gave you coordinates, or made a joke of you.

Any coordinates outside this range are invalid:
Valid latitude must be between -90 and 90
Valid longitude must be between -180 and 180

If input is valid, you have accurate information from your boss, so can proceed to next step.
If the input is invalid return "I am claiming extra holiday!" since your boss is making joke at your expense.

2. You are expected to get optinal solution, best possible option what in this case means shortest distance

To calculate distance, use Haversine formula, with EARTH_RADIUS = 3959, due to working in miles.

Remember, you need to get best out of 24 possible travel options (because you have to visit 4 customers,
you have 24 possible combinations to choose from). Do not forget that you need to travel from the office to
first customer and back to the office from last customer.

3. Calculate your expences

You are not expected to round decimal numbers at any point of this kata(rounding during calculation process,
may fail testing), and your boss is so good to you, that he accepts 0.01% tolerance between your calculation
and his expectation.
"""

import itertools
import math

# Constants.
EARTH_RADIUS = 3959  # Radius of Earth in miles.
EXPENSE_PER_MILE = 10  # Expense per mile.
BASE_EXPENSE = 500  # Base expense.
OFFICE = {"lat": 51.49984, "long": -0.124663}  # Office coordinates.


def validate_coordinates(coords):
    for coord in coords:
        if not (-90 <= coord['lat'] <= 90 and -180 <= coord['long'] <= 180):
            return False
    return True


def haversine_distance(lat1, long1, lat2, long2):
    # Convert latitude and longitude from degrees to radians.
    lat1_rad = math.radians(lat1)
    long1_rad = math.radians(long1)
    lat2_rad = math.radians(lat2)
    long2_rad = math.radians(long2)
    
    # Haversine formula.
    dlon = long2_rad - long1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS * c
    return distance


def travel_expenses(customers):
    if not validate_coordinates(customers):
        return "I am claiming extra holiday!"
    
    # Generate all permutations of customers.
    customer_permutations = list(itertools.permutations(customers))
    min_distance = float('inf')
    optimal_route = None
    
    for perm in customer_permutations:
        total_distance = 0
        # Calculate total distance for this permutation.
        current_location = OFFICE
        for customer in perm:
            total_distance += haversine_distance(current_location['lat'], current_location['long'], 
                                                 customer['lat'], customer['long'])
            current_location = customer
        # Add return to office distance.
        total_distance += haversine_distance(current_location['lat'], current_location['long'], 
                                             OFFICE['lat'], OFFICE['long'])
        
        # Check if this permutation gives minimum distance.
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_route = perm
    
    # Calculate expenses.
    total_expense = BASE_EXPENSE + (min_distance * EXPENSE_PER_MILE)
    
    return int(total_expense)
