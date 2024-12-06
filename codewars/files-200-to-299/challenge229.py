"""
Write a function that returns the total surface area and volume of a box as an array: [area, volume].
"""


def get_size(w, h, d):
    # Calculate surface area.
    surface_area = 2 * (w * h + h * d + w * d)
    
    # Calculate volume.
    volume = w * h * d
    
    # Return the result as an array.
    return [surface_area, volume]
