"""
The Stanton measure of an array is computed as follows:

- Count the number of occurences for value 1 in the array and let this count be n.

The Stanton measure is the number of times that n appears in the array.

Write a function which takes an integer array and returns its Stanton measure.
"""


def stanton_measure(arr):
  n = arr.count(1)
  return arr.count(n)
