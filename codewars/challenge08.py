"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the
same value next to each other and preserving the original order of elements.

Examples:
1) unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'].
2) unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D'].
3) unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3].
4) unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3].
"""


def unique_in_order(sequence):
    unique_list = []
    prev_element = None
    
    for element in sequence:
        if element != prev_element:
            unique_list.append(element)
            prev_element = element
            
    return unique_list

test_cases = [
    'AAAABBBCCDAABBB',  # ['A', 'B', 'C', 'D', 'A', 'B']
    'ABBCcAD',          # ['A', 'B', 'C', 'c', 'A', 'D']
    [1, 2, 2, 3, 3],    # [1, 2, 3]
    (1, 2, 2, 3, 3)     # [1, 2, 3]
]

results = [unique_in_order(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"unique_in_order({case}) == {result}")
