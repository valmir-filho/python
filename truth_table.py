# TRUTH TABLE

"""
Logical Operator "and".

P   Q  Result
V   V    V
V   F    F
F   V    F
F   F    F


Logical Operator "or".

P   Q  Result
V   V    V
V   F    V
F   V    V
F   F    F
"""

# Practice tests.

# Logical Operator "and".

print('Truth Table Logical Operator "and".')

# Case 1
P1 = True
Q1 = True
result = P1 and Q1
print(f"P(True) and Q(True) = {result}.")

# Case 2
P2 = True
Q2 = False
result = P2 and Q2
print(f"P(True) and Q(False) = {result}.")

# Case 3
P3 = False
Q3 = True
result = P3 and Q3
print(f"P(False) and Q(True) = {result}.")

# Case 4
P4 = False
Q4 = False
result = P4 and Q4
print(f"P(False) and Q(False) = {result}.")


print()

# Logical Operator "or".

print('Truth Table Logical Operator "or".')

# Case 1
R1 = True
S1 = True
result = R1 or S1
print(f"R(True) or S(True) = {result}.")

# Case 2
R2 = True
S2 = False
result = R2 or S2
print(f"R(True) or S(False) = {result}.")

# Case 3
R3 = False
S3 = True
result = R3 or S3
print(f"R(False) or S(True) = {result}.")

# Case 4
R4 = False
S4 = False
result = R4 or S4
print(f"R(False) or S(False) = {result}.")
