"""
It's the academic year's end, fateful moment of your school report.
The averages must be calculated. All the students come to you and entreat
you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
"""


def calculate_average(grades):
    # Calculate the sum of all grades in the array.
    total_sum = sum(grades)
    # Find the number of grades.
    num_of_grades = len(grades)
    # Calculate the average.
    average = total_sum / num_of_grades
    # Round down the average to the nearest integer and return it.
    return int(average)  # Using int() to round down because it truncates the decimal part.

# Usage example.
grades = [70, 80, 90]  # Replace this with any array of grades.
average_grade = calculate_average(grades)
print(average_grade)
