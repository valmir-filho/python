"""
Given an array with 3 subarrays, each containing hexadecimal color codes loosely defining red, green and blue colors based on their predominant byte value,
return a string description of which of the three colors each array contains.

Input is an array which contains 3 subarrays. These subarrays contain strings representing colors in RGB format, each string will contain one predominant color
channel that is more saturated than the other two. Among all the strings in an subarray only 2 color channels will come up as predominant - the one that appears
more often is "major" and the one that appears less often is "minor". Your task is to determine the major and minor colors inside each subarray and return them in
the following format: {Major1}+{Minor1},{Major2}+{Minor2},{Major3}+{Minor3}.

Example:

input = [
  ["FFA07A", "FA8072", "8DC4DE"],
  ["7FFF00", "ADFF2F", "FF0000", "00FF7F", "00FF7F"],
  ["ADD8E6", "6B8E23", "9ACD32", "32CD32", "00FF00"]
]

result = "Red+Blue,Green+Red,Green+Blue"

Explanation:
- first subarray's predominant colors: Red, Red, Blue (Red is major, Blue is minor).
- second subarray's predominant colors: Green, Green, Red, Green, Green (Green is major, Red is minor).
- third subarray's predominant colors: Blue, Green, Green, Green, Green (Green is major, Blue is minor).
"""


def get_colors(col_arr):
    def predominant_color(hex_color):
        """Retorna o canal predominante (Red, Green ou Blue) de uma cor hexadecimal."""
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        max_val = max(r, g, b)
        if r == max_val:
            return "Red"
        elif g == max_val:
            return "Green"
        else:
            return "Blue"

    result = []
    for subarray in col_arr:
        counts = {"Red": 0, "Green": 0, "Blue": 0}
        for hex_color in subarray:
            color = predominant_color(hex_color)
            counts[color] += 1

        # Ordena pela contagem (maior → menor).
        sorted_colors = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        major = sorted_colors[0][0]
        minor = next((c for c, n in sorted_colors[1:] if n > 0), None)
        result.append(f"{major}+{minor}")

    return ",".join(result)

# Exemplo de uso:
input_data = [
    ["FFA07A", "FA8072", "8DC4DE"],
    ["7FFF00", "ADFF2F", "FF0000", "00FF7F", "00FF7F"],
    ["ADD8E6", "6B8E23", "9ACD32", "32CD32", "00FF00"]
]

print(get_colors(input_data))
# Saída esperada: "Red+Blue,Green+Red,Green+Blue".
