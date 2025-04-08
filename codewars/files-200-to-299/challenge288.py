"""
Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses ().
In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

Notes
- The numbers are always positive, in the range 1 ≤ a, b, c ≤ 10;
- You can use the same operation more than once;
- It is not necessary to use all the operators or parentheses;
- You cannot swap the operands. For example, with the given numbers, you cannot get the expression (1 + 3) * 2 = 8;

Input and Output Examples
- expressionsMatter(1, 2, 3) ==> 9, because (1 + 2) * 3 = 9;
- expressionsMatter(1, 1, 1) ==> 3, because 1 + 1 + 1 = 3;
- expressionsMatter(9, 1, 1) ==> 18, because 9 * (1 + 1) = 18.
"""


def expression_matter(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        a + b * c,
        a * b + c,
        (a + b) * c,
        a * (b + c)
    )
