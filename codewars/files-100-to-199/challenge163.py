"""
Your task is to split the chocolate bar of given dimension n x m into small squares.
Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.
For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break,
but for size 3 x 1 you must do two breaks. If input data is invalid you should return 0
(as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
"""


def break_chocolate(n, m):
    # If either dimension is 0, or both are 0, no breaks are needed.
    if n <= 0 or m <= 0:
        return 0
    # Calculate the minimum number of breaks needed.
    return (n * m) - 1
  
