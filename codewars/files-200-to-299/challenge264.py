"""
Complete the function that receives as input a string, and produces outputs according to the following table:

Input	             Output
"Jabroni"	         "Patron Tequila"
"School Counselor" "Anything with Alcohol"
"Programmer"	     "Hipster Craft Beer"
"Bike Gang Member" "Moonshine"
"Politician"	     "Your tax dollars"
"Rapper"	         "Cristal"
"anything else"    "Beer"

Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer".

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, the input "pOLitiCIaN" should still return "Your tax dollars".
"""


def get_drink_by_profession(param):
    # Dictionary mapping professions to drinks.
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    
    # Normalize input to lowercase and fetch the corresponding drink.
    return drinks.get(param.lower(), "Beer")
