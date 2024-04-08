"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the
opportunity to go for a short walk. The city provides its citizens with a Walk
Generating App on their phones -- everytime you press the button it sends you an
array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block for each letter (direction) and you know it takes
you one minute to traverse one city block, so create a function that will return true
if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters
('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
"""


def is_valid_walk(walk):
    # Check if walk is exactly 10 minutes.
    if len(walk) != 10:
        return False
    
    # Count occurrences of each direction.
    north_south = walk.count('n') - walk.count('s')
    east_west = walk.count('e') - walk.count('w')
    
    # Check if walk returns to starting point.
    return north_south == 0 and east_west == 0

# Usage examples.
walk = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']
print(is_valid_walk(walk))  # This should return True.

walk = ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'e', 'w']
print(is_valid_walk(walk))  # This might return False based on the direction counts.
