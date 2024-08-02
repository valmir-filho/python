"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
"""


def validate_pin(pin):
    # Check if the length of the PIN is either 4 or 6.
    if len(pin) == 4 or len(pin) == 6:
        # Check if all characters in the PIN are digits
        return pin.isdigit()
    # Return False if the length is not 4 or 6.
    return False
  
