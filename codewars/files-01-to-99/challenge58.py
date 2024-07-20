"""
Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""


def format_time(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Seconds must be a non-negative integer less than or equal to 359999.")

    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
