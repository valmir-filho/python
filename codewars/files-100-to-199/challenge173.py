"""
A hero is on his way to the castle to complete his mission.
However, he's been told that the castle is surrounded with a
couple of powerful dragons! each dragon takes 2 bullets to be
defeated, our hero has no idea how many bullets he should carry.
Assuming he's gonna grab a specific given number of bullets and
move forward to fight another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)
"""


def hero(bullets, dragons):
    # Each dragon needs 2 bullets, so the hero needs 2 times the number of dragons.
    return bullets >= 2 * dragons
