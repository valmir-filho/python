"""
For a given string s we are looking for the number of distinct substrings of s.

For example, the distinct substrings of "aab" are "", "a", "b", "aa", "ab", "aab".

A naive solution like counting all distinct substrings would be far too slow here.
Instead we could derive the requested information from the set of all suffixes of s.
This should be possible, because every substring of s is a prefix of a suffix of s.

You should be able to pass the tests of this kata just by following the described idea.
You won't need any special algorithm. However, you should let Python do the job with builtin functions whereever possible instead of re-implementing functions with for-loops.

Expect the following in the random tests:

- 10 strings of length <= 1_000;
- 10 strings of length <= 2_000;
- 10 strings of length <= 4_000;
- 5 strings of length <= 20_000.
"""

from os.path import commonprefix


def number_of_substrings(s: str) -> int:
    """count number of distinct substrings of given string s"""

    n = len(s)
    suffixes = sorted(s[i:] for i in range(n))

    repeated = 0
    previous = ""

    for suffix in suffixes:
        repeated += len(commonprefix((previous, suffix)))
        previous = suffix

    return 1 + n * (n + 1) // 2 - repeated
