"""
Your task in order to complete this Kata is to write a function
which formats a duration, given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""


def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    # Define time units in seconds.
    units = {
        'year': 31536000,  # 60 * 60 * 24 * 365
        'day': 86400,      # 60 * 60 * 24
        'hour': 3600,      # 60 * 60
        'minute': 60,
        'second': 1
    }
    
    # Calculate the number of each time unit.
    result = []
    for unit, value in units.items():
        count, seconds = divmod(seconds, value)
        if count > 0:
            result.append(f"{count} {unit}{'s' if count > 1 else ''}")
    
    # Join the results with commas and "and".
    if len(result) == 1:
        return result[0]
    return ', '.join(result[:-1]) + ' and ' + result[-1]
