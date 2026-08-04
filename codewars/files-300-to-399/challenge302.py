""
You have a string of numbers, starting with the third number each number is the result of an operation performed using the previous two numbers.

Complete the function which returns a string of the operations in order and separated by a comma and a space, e.g. "subtraction, subtraction, addition".

The available operations are (in this order of preference):

- 1) addition;
- 2) subtraction;
- 3) multiplication;
- 4) division.

Notes:

- All input data is valid;
- The number of numbers in the input string >= 3;
- For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list (in this case "addition");
- Integer division should be used.
"""


def say_me_operations(string_numbers):
    numbers = list(map(int, string_numbers.split()))
    operations = []
    
    for i in range(2, len(numbers)):
        a, b, c = numbers[i-2], numbers[i-1], numbers[i]
        
        if a + b == c:
            operations.append("addition")
        elif a - b == c:
            operations.append("subtraction")
        elif a * b == c:
            operations.append("multiplication")
        elif b != 0 and a // b == c:
            operations.append("division")
        else:
            operations.append("unknown")  # para garantir que não quebre, embora você tenha dito que o input é sempre válido.

    return ", ".join(operations)
