"""
A child is playing with a ball on the nth floor of a tall building.
The height of this floor above ground level, h, is known.
He drops the ball out of the window. The ball bounces (for example),
to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her
window (including when it's falling and bouncing)?

Three conditions must be met for a valid experiment:
- Float parameter "h" in meters must be greater than 0;
- Float parameter "bounce" must be greater than 0 and less than 1;
- Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer,
otherwise return -1.

Note: The ball can only be seen if the height of the rebounding ball is
strictly greater than the window parameter.
"""


def bouncing_ball(h, bounce, window):
    # Validate the input parameters.
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    count = 0
    
    while h > window:
        # When the ball is falling.
        count += 1
        # Ball bounces.
        h *= bounce
        # When the ball is bouncing up, it is visible only if it passes the window height.
        if h > window:
            count += 1
    
    return count
