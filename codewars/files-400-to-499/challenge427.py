"""
Ava, Mark, Sheila, and Pete are at a party. However, Ava and Sheila are only staying if there are at least 4 people,
Pete is only staying if there's at least 1 person, and Mark is only staying if there are at least 5 people.
Therefore, Mark leaves, which makes Ava and Sheila leave, and Pete is left alone.

Given an array with the preferences of every person at a party for the minimum number of people present, determine how many people will stay.

Examples:

[4, 5, 4, 1] ➞ 1
# Ava's minimum number is 4, Mark's is 5, Sheila's is 4, and Pete's is 1.
# Only 1 person (Pete) stays.

[10, 12, 15, 15, 5] ➞ 0

[2, 1, 2, 0] ➞ 4

Notes:

- All attendees are included in the array;
- Any person's count of people currently at the party includes themself;
- A persons preference minimum can be 0, 1, or any positive integer;
- Expect valid input only;
- 0 <= len(lst) <= 10^5.
"""


def party_people(lst):
    n = len(lst)
    
    while True:
        # filtra quem pode ficar.
        new_lst = [x for x in lst if x <= n]
        
        # se ninguém saiu, terminou.
        if len(new_lst) == n:
            return n
        
        # atualiza lista e tamanho.
        lst = new_lst
        n = len(lst)
