"""
Your friend has been out shopping for puppies (what a time to be alive!).
He arrives back with multiple dogs, and you simply do not know how to respond!
By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.
The number of dogs will always be a number and there will always be at least 1 dog.
"""


def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        respond = dogs[0]  # Less than or equal to 10 dogs.
    elif n <= 50:
        respond = dogs[1]  # Between 11 and 50 dogs.
    elif n == 101:
        respond = dogs[3]  # Exactly 101 dogs.
    else:
        respond = dogs[2]  # More than 50 dogs but not 101.
    return respond
