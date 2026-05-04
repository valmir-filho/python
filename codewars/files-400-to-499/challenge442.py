"""
The number 1089 is the smallest one, non palindromic, that has the same prime factors that its reversal. Thus,

prime factorization of 1089 with 3, 3, 11, 11 -------> 3, 11

prime factorization of 9801 with  3, 3, 3, 3, 11, 11 -------> 3, 11

The task for this kata is to create a function same_factRev(), that receives a nMax, to find all the numbers with the above property, bellow nMax.

the function same_factRev(), will output a sorted list with the found numbers bellow nMax

Let'se some cases:

same_factRev(1100) -----> [1089]

same_factRev(2500) -----> [1089, 2178]

(Palindromic numbers are like: 171, 454, 4224, these ones should be discarded)

Happy coding!!

(The sequence of these kind of numbers is registered in OEIS as A110819)
"""


def same_fact_rev(n_max):
    def reverse_num(n):
        return int(str(n)[::-1])

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def prime_factors_set(n):
        factors = set()
        d = 2

        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1 if d == 2 else 2  # depois do 2, testa só ímpares.

        if n > 1:
            factors.add(n)

        return factors

    result = []

    for n in range(1, n_max):
        if is_palindrome(n):
            continue

        rev = reverse_num(n)

        if prime_factors_set(n) == prime_factors_set(rev):
            result.append(n)

    return result
