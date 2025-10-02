"""
In information theory and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences.
Informally, the Levenshtein distance between two words is the minimum number of single-character edits (i.e. insertions, deletions or substitutions) required to change one word into the other.

Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.
"""


def levenshtein(a: str, b: str) -> int:
    # Cria uma matriz (len(a)+1) x (len(b)+1).
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Inicializa a primeira linha e primeira coluna.
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    # Preenche a matriz.
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # remoção.
                dp[i][j - 1] + 1,      # inserção.
                dp[i - 1][j - 1] + cost  # substituição.
            )

    return dp[len(a)][len(b)]


# Exemplo de uso.
if __name__ == "__main__":
    print(levenshtein("kitten", "sitting"))  # saída: 3.
    print(levenshtein("flaw", "lawn"))       # saída: 2.
