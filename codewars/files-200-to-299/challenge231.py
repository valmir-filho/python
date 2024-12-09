"""
Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.

CONDITIONS
- Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value;
- If the value is the same they both perish;
- If one of the values is empty(different array lengths) the non-empty value soldier survives;
- To survive the defending side must have more survivors than the attacking side;
- In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. If the total attack power of both sides is the same return true;
- The initial attack power is the sum of all the values in each array.
"""


def is_defended(attackers, defenders):
    # Initialize survivor counts.
    attacker_survivors = 0
    defender_survivors = 0

    # Determine the minimum length of the arrays.
    min_length = min(len(attackers), len(defenders))

    # Compare soldiers at the same indices.
    for i in range(min_length):
        if attackers[i] > defenders[i]:
            attacker_survivors += 1
        elif attackers[i] < defenders[i]:
            defender_survivors += 1
        # If equal, both perish, do nothing.

    # Handle extra soldiers in longer array.
    if len(attackers) > len(defenders):
        attacker_survivors += len(attackers) - len(defenders)
    elif len(defenders) > len(attackers):
        defender_survivors += len(defenders) - len(attackers)

    # Decide the result based on survivor counts.
    if defender_survivors > attacker_survivors:
        return True
    elif attacker_survivors > defender_survivors:
        return False
    else:
        # Compare total initial power if survivors are tied.
        attacker_power = sum(attackers)
        defender_power = sum(defenders)
        return defender_power >= attacker_power
