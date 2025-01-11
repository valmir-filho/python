"""
Create a function called _if which takes 3 arguments: a value bool and 2 functions (which do not take any parameters): func1 and func2.

When bool is truthy, func1 should be called, otherwise call the func2.
"""


def _if(condition, func1, func2):
    if condition:
        func1()
    else:
        func2()


# Usage example.
def truthy(): 
    print("True")


def falsey(): 
    print("False")
  
_if(True, truthy, falsey)  # prints 'True'.
_if(False, truthy, falsey)  # prints 'False'.
