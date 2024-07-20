"""
To find the volume (centimeters cubed) of a cuboid you use the formula: volume = Length * Width * Height.
But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!
It's up to you to find out whether the cuboid has equal sides (= is a cube).
Return true if the cuboid could have equal sides, return false otherwise.
Return false for invalid numbers too (e.g volume or side is less than or equal to 0).
Note: side will be an integer.
"""


def is_cube(volume, side):
    if volume <= 0 or side <= 0:
        return False
   
    expected_volume = side ** 3
    
    return volume == expected_volume
