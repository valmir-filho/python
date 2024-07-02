"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values
will result in a hexadecimal representation being returned. Valid decimal values
for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
"""


def rgb(r, g, b):
    # Clamp the values to the range 0-255.
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    # Convert to hexadecimal and format as 6-character string.
    return '{:02X}{:02X}{:02X}'.format(r, g, b)
