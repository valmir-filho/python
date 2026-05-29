"""
Definition: A Tidy Number is a number whose digits are in non-decreasing order.

Task: Given a number, determine if it is tidy or not.

Notes:

- The number passed will always be positive;
- Return the result as a boolean.

Examples:

12 ==> return true
Explanation: Digits {1, 2} are in non-decreasing order (1 <= 2).

32 ==> return false
Explanation: Digits {3, 2} are not in non-decreasing order (3 > 2).

1024 ==> return false
Explanation: Digits {1, 0, 2, 4} are not in non-decreasing order (1 > 0).

13579 ==> return true
Explanation: Digits {1, 3, 5, 7, 9} are in non-decreasing order.

2335 ==> return true
Explanation: Digits {2, 3, 3, 5} are in non-decreasing order (3 = 3).

- Playing with Numbers Series;
- Playing With Lists/Arrays Series;
- For More Enjoyable Katas;
- ALL translations are welcomed.

Enjoy Learning!!

Zizou
"""


def tidyNumber(n):
    s = str(n)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))
