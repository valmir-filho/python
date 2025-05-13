"""
You need to write regex that will validate a password to make sure it meets the following criteria:

- At least six characters long;
- Contains a lowercase letter;
- Contains an uppercase letter;
- Contains a digit;
- Only contains alphanumeric characters (note that '_' is not alphanumeric).
"""

import re

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$'
