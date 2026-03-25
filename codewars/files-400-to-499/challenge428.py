"""
Linked Lists - Sorted Insert

Write a SortedInsert() function which inserts a node into the correct location of a pre-sorted linked list which is sorted in ascending order.
SortedInsert takes the head of a linked list and data used to create a node as arguments. SortedInsert() should also return the head of the list.

sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

The push() and buildOneTwoThree() functions do not need to be redefined.


Related Kata in order of expected completion (increasing difficulty):

- Linked Lists - Push & BuildOneTwoThree;
- Linked Lists - Length & Count;
- Linked Lists - Get Nth Node;
- Linked Lists - Insert Nth Node;
- Linked Lists - Sorted Insert;
- Linked Lists - Insert Sort;
- Linked Lists - Append;
- Linked Lists - Remove Duplicates;
- Linked Lists - Move Node;
- Linked Lists - Move Node In-place;
- Linked Lists - Alternating Split;
- Linked Lists - Front Back Split;
- Linked Lists - Shuffle Merge;
- Linked Lists - Sorted Merge;
- Linked Lists - Merge Sort;
- Linked Lists - Sorted Intersect;
- Linked Lists - Iterative Reverse;
- Linked Lists - Recursive Reverse.

Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.
"""


def sorted_insert(head, data):
    new_node = Node(data)

    # Caso 1: lista vazia ou inserir no início.
    if head is None or data < head.data:
        new_node.next = head
        return new_node

    # Caso 2: encontrar posição correta.
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    # Inserção.
    new_node.next = current.next
    current.next = new_node

    return head
