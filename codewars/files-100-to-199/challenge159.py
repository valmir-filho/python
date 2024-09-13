"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
"""


def is_valid_IP(strng):
    # Split the string by dots.
    parts = strng.split('.')
    
    # Check if there are exactly 4 parts.
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a digit and has no leading zeros.
        if not part.isdigit() or (part != str(int(part))):
            return False
        
        # Convert the part to an integer and check if it is in the valid range.
        if not (0 <= int(part) <= 255):
            return False
    
    return True
