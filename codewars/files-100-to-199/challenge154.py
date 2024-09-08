"""
Create a function that takes a number as an argument and returns a grade based on that number.

Score	Grade

Anything greater than 1 or less than 0.6:	"F"
0.9 or greater:	"A"
0.8 or greater:	"B"
0.7 or greater:	"C"
0.6 or greater:	"D"
"""


def grader(score):
    # Check for invalid scores.
    if score > 1 or score < 0.6:
        return 'F'
    
    # Check for each grade range in descending order of precedence
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        # For completeness, though it should not be needed.
        return "F"
