"""
You are sitting comfortably in your sofa, well within the comforts of your home.
You type furiously on your keyboard - unable to solve a frustrating codewars problem.
Suddenly, you feel you are falling in an endless pit. You land in The Depths Of Tartarus.

You shall receive a string in the input. Your task is simple.
You have to see through the clouds(Achlys OR Nephos) that are preventing you to see the monsters that surround you.

Notes:

Monster name letters are in order.

If more than one monster name can be found as an ordered subsequence, return the one that starts first.

For Example (contains ALL possible monsters):

i) Hydra 🐉
H3yD1rA7F2q8M5x6Z0!

ii)Nekros ☠️
nE2kR3o5S6v0P4t8X1

iii)Cyclops 👁️
cY1cL0o9p5S8b6T3Q2

iv) Minotaur 🐂
M1i4nO7tA2u9R5k0L6/

v) Cerberus 𓃦
C3e1rB2e5R6u4S7!9

vi)Chimera 🐐🔥
C2hI4m3eR5a8F1l0x6

vii) Harpy 🕊️💀
H1a3R4p2Y5q0!8

viii) Gorgon 🐍👁️
G4o1R2g0O5n8X6!

ix) Kraken 🐙
K1r3a5k2E4n0!9

x) Siren 🧜‍♀️🎵
S2i1R3e0N5x8Q7!

xi) Furies ⚡😡
F1u2R3i5E4s6Z0!

xii) Satyr 🐐🎶
S2a1T3y0R4q5!6
"""


def detect_monster(s):
    monsters = [
        "Hydra", "Nekros", "Cyclops", "Minotaur", "Cerberus", "Chimera",
        "Harpy", "Gorgon", "Kraken", "Siren", "Furies", "Satyr"
    ]

    if not s:
        return "None"

    sl = s.lower()

    def earliest_match(word: str):
        w = word.lower()
        first = w[0]

        # try every possible start position for the first letter, left-to-right.
        for i, ch in enumerate(sl):
            if ch != first:
                continue

            pos = i
            ok = True

            # greedily find subsequent letters after the current position.
            for wc in w[1:]:
                nxt = sl.find(wc, pos + 1)
                if nxt == -1:
                    ok = False
                    break
                pos = nxt

            if ok:
                # i = start index, pos = end index.
                return (i, pos, word)

        return None

    best = None
    for m in monsters:
        res = earliest_match(m)
        if res is None:
            continue
        if best is None or (res[0], res[1]) < (best[0], best[1]):
            best = res

    return best[2] if best else "None"
