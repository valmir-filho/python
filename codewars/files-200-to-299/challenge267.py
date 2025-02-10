"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
"""

from ipaddress import ip_address


def ips_between(start: str, end: str) -> int:
    return int(ip_address(end)) - int(ip_address(start))
