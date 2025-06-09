"""
A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z.
Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.

Task

You will receive the bookseller's stocklist and a list of categories.
Your task is to find the total number of books in the bookseller's stocklist,
with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

Example

The bookseller's stocklist:
"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"

List of categories: 
"A", "B", "C", "W"

Result:
"(A : 20) - (B : 114) - (C : 50) - (W : 0)"

Explanation:
Category A: 20 books (ABART)
Category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
Category C: 50 books (CDXEF)
Category W: 0 books
"""


def stock_list(stocklist, categories):
    # If either list is empty, return an empty string as per the requirements.
    if not stocklist or not categories:
        return ""

    # Create a dictionary to hold the counts for each requested category, initialized to 0.
    # This ensures that even categories with no matching books are included in the result.
    category_counts = {cat: 0 for cat in categories}

    # Iterate over each entry in the bookseller's stocklist.
    for item in stocklist:
        # The first character of the code is the book's category.
        category = item[0]
        
        # Check if this category is one of the ones we're interested in.
        if category in category_counts:
            # The item is a string like "CODE QUANTITY". We split it by the space
            # to separate the code and the quantity. The quantity is the second part.
            # We convert the quantity string to an integer and add it to the total for that category.
            quantity = int(item.split(' ')[1])
            category_counts[category] += quantity
            
    # Build the formatted result string.
    # We iterate through the original `categories` list to maintain the correct order.
    # For each category, we create a string like "(CATEGORY : COUNT)".
    result_parts = [f"({cat} : {category_counts[cat]})" for cat in categories]
    
    # Join all the parts together with " - " as the separator.
    return " - ".join(result_parts)
