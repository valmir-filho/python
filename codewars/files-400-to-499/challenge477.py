"""
Number is a palindrome if it is equal to the number with digits in reversed order.
For example, 5, 44, 171, 4884 are palindromes, and 43, 194, 4773 are not.

Write a function which takes a positive integer and returns the number of special steps needed to obtain a palindrome.
The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome,
repeat the procedure with the sum until the resulting number is a palindrome.

If the input number is already a palindrome, the number of steps is 0.

All inputs are guaranteed to have a final palindrome smaller than 263.

Example:

For example, start with 87:

  87 +   78 =  165     - step 1, not a palindrome
 165 +  561 =  726     - step 2, not a palindrome
 726 +  627 = 1353     - step 3, not a palindrome
1353 + 3531 = 4884     - step 4, palindrome!

4884 is a palindrome and we needed 4 steps to obtain it, so answer for 87 is 4.

Additional info: some interesting information on the problem can be found in this Wikipedia article on Lychrel numbers.
"""


def palindrome_chain_length(n):
    steps = 0

    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        steps += 1

    return steps
