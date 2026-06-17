"""
This kata is the performance version of Don't give me five by user5036852.

Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).

You are given the start and the end of the integer range. The start and the end are both inclusive.

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> return 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12

The result may contain fives. ;-)

The start will always be smaller than the end. Both numbers can be also negative.

The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!

Good luck, warrior!
"""


def dont_give_me_five(start, end):
    def count_until(n):
        """Conta números de 0 até n que não têm o dígito 5."""
        if n < 0:
            return 0

        digits = str(n)
        total = 0
        length = len(digits)

        for i, ch in enumerate(digits):
            d = int(ch)
            remaining = length - i - 1

            # quantos dígitos menores que d não são 5
            choices = sum(1 for x in range(d) if x != 5)

            total += choices * (9 ** remaining)

            if d == 5:
                return total

        return total + 1

    if start >= 0:
        return count_until(end) - count_until(start - 1)

    if end < 0:
        return count_until(-start) - count_until(-end - 1)

    return (count_until(-start) - 1) + count_until(end)
