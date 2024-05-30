"""
Given two arrays a and b write a function comp(a, b) that checks
whether the two arrays have the "same" elements, with the same
multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless
of the order.
"""


def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False

    count1 = {}
    count2 = {}

    for num in array1:
        squared = num * num
        if squared in count1:
            count1[squared] += 1
        else:
            count1[squared] = 1

    for num in array2:
        if num in count2:
            count2[num] += 1
        else:
            count2[num] = 1

    return count1 == count2
