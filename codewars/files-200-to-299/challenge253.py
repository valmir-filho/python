"""
Character recognition software is widely used to digitise printed texts.
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

- S is misinterpreted as 5;
- O is misinterpreted as 0;
- I is misinterpreted as 1.

The test cases contain numbers only by mistake.
"""


def correct(s):
    # Replace incorrect characters with their correct counterparts.
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')
