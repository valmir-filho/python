"""
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)
"john McClane" --> "McClane john"
"""


def swap_names(full_name):
    # Split the full name into first name and last name.
    names = full_name.split()
    
    # Check if there are at least two names.
    if len(names) >= 2:
        # Swap the first name with the last name
        names[0], names[-1] = names[-1], names[0]
        
        # Join the names back into a string.
        swapped_name = ' '.join(names)
        return swapped_name
    else:
        return "Please provide a full name with at least two names."

# Example usage.
original_name = "John McClane"
swapped_name = swap_names(original_name)
print(swapped_name)  # Output will be "McClane John"
