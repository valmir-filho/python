"""
This kata is inspired by Totally Good Permutations, a string-based version of this problem.

Overview

Imagine you are given a list of "bad numbers". We shall say that a number is "totally good" if it does not contain all the distinct digits of any bad number.

For a given list of bad numbers and two integers a and b, how many numbers between a and b inclusive are totally good?

Example

Let's take bad = [582, 533, 34] for example, we have: 
258, 285, 528, 825, 852 are not totally good (permutations of 582)
554433 is not totally good (having all digits from both 533 and 34)
35 and 53 are not totally good (having 3 and 5 from 533)
3, 5, 456789 are totally good

Input Constraints

0 ≤ bad[i] ≤ 10^15

Fixed test cases: 0 ≤ |bad| ≤ 3, 0 ≤ a ≤ b ≤ 100 (one hundred)
Small test cases: 0 ≤ |bad| ≤ 6, 0 ≤ a ≤ b ≤ 10^5 (one hundred thousand)
Medium test cases: 0 ≤ |bad| ≤ 9, 0 ≤ a ≤ b ≤ 10^10 (ten billion)
Large test cases: 0 ≤ |bad| ≤ 12, 0 ≤ a ≤ b ≤ 10^15 (one quadrillion)
"""


def totally_good(a, b, bad):
    """
    Calculates the number of "totally good" integers between a and b, inclusive.
    A number is totally good if it does not contain all the distinct digits of any bad number.
    This solution uses a digit dynamic programming approach for efficiency.
    """

    # Helper class to encapsulate the state for the digit DP solver.
    class Solver:
        def __init__(self, bad_numbers):
            self.memo = {}
            self.s = ""
            self.bad_masks = self._preprocess_bad(bad_numbers)

        def _preprocess_bad(self, bad_numbers):
            if not bad_numbers:
                return []

            # 1. Get unique sets of digits for each bad number.
            digit_sets = set()
            for n in bad_numbers:
                s_n = str(n)
                current_set = frozenset(map(int, s_n))
                digit_sets.add(current_set)
            
            # 2. Filter to keep only minimal sets to avoid redundant checks.
            minimal_sets = []
            sorted_sets = sorted(list(digit_sets), key=len)

            for s1 in sorted_sets:
                is_redundant = False
                for s2 in minimal_sets:
                    if s2.issubset(s1):
                        is_redundant = True
                        break
                if not is_redundant:
                    minimal_sets.append(s1)
            
            # 3. Convert minimal sets to bitmasks for efficient checking.
            bad_masks = []
            for s in minimal_sets:
                mask = 0
                for digit in s:
                    mask |= (1 << digit)
                bad_masks.append(mask)
            return bad_masks

        def _is_good(self, mask):
            # The number 0, represented by a path of leading zeros, results in mask=0.
            # Its actual digit set is {0}, so its effective mask is 1 (1 << 0).
            if mask == 0:
                mask = 1
            
            for bad_mask in self.bad_masks:
                # Check if the number's digit set is a superset of any bad set.
                if (mask & bad_mask) == bad_mask:
                    return False
            return True

        def _dp(self, index, tight, is_leading, mask):
            # Base case: we have constructed a full number.
            if index == len(self.s):
                return 1 if self._is_good(mask) else 0

            # Memoization to avoid recomputing states.
            state = (index, tight, is_leading, mask)
            if state in self.memo:
                return self.memo[state]

            ans = 0
            limit = int(self.s[index]) if tight else 9

            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)

                if is_leading and digit == 0:
                    # Still processing leading zeros; the mask remains 0.
                    ans += self._dp(index + 1, new_tight, True, 0)
                else:
                    # Processing a non-zero digit or are past leading zeros.
                    new_mask = mask | (1 << digit)
                    ans += self._dp(index + 1, new_tight, False, new_mask)
            
            self.memo[state] = ans
            return ans

        def count_good_up_to(self, n_str):
            # Handle the edge case for counting up to a-1 when a=0.
            if n_str == "-1":
                return 0
            self.s = n_str
            self.memo.clear()
            # The DP counts good numbers in the range [0, n].
            return self._dp(0, True, True, 0)

    solver = Solver(bad)
    
    count_b = solver.count_good_up_to(str(b))
    count_a_minus_1 = solver.count_good_up_to(str(a - 1))
    
    return count_b - count_a_minus_1
