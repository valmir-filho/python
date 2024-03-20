"""
A square of squares.

You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them
into a square of square building blocks! However, sometimes, you can't arrange them into a square. Instead, you end up with an
ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's
it! You just have to check if your number of building blocks is a perfect square.

Task: Given an integral number, determine if it's a square number. In mathematics, a square number or perfect square is an integer
that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples:
1) -1  =>  false.
2)  0  =>  true.
3)  3  =>  false.
4)  4  =>  true.
5) 25  =>  true.
6) 26  =>  false.
"""


def is_square(n):
    return n >= 0 and int(n**0.5)**2 == n

# Usage examples.

print(is_square(16))  # True.
print(is_square(25))  # True.
print(is_square(14))  # False.
