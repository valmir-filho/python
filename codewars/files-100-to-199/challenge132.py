"""
Description

You are fleeing from enemies through a maze. You need to reach the exit through many rooms that are laid out in a straight line.
Some rooms have a light bulb. If the light bulb is lit when you enter the room, the enemy will see you and you will be caught.
In other words, you can only walk in the darkness. Fortunately, the status of these bulbs (on/off) is switched automatically every minute.
So you have a chance to go through the maze, if the lightbulbs are turned off at the right time.
You have to be constantly on the move, otherwise the enemy will catch up to you.

Specifications

The rooms are represented by a string, e.g. "xo oxox".

'x' means there is a bulb in the room, and its initial status is off
'o' means there is a bulb in the room, and its initial status is on
' '(space) means a room without bulb, it is always dark.
Your task is to determine if you can go through the maze. Return true if you can, false otherwise.

Notes

Your initial position is at the leftmost room; the exit position is at the rightmost.
Your moving speed is 1 minute per room. You have to keep moving constantly, i.e. you cannot wait for the next room to become dark.
You have to start moving immediately.
"""


def bulb_maze(maze):
    for i, room in enumerate(maze):
        if room == 'o' and i % 2 == 0:
            # Bulb is on in this room at even index, you get caught.
            return False
        elif room == 'x' and i % 2 != 0:
            # Bulb is on in this room at odd index, you get caught.
            return False
    return True
