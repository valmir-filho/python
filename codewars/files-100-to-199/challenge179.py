"""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string.
"""

from urllib.parse import urlparse


def domain_name(url):
    # Parse the URL.
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Handle cases where the URL does not have a protocol (e.g., "xakep.ru").
    if not domain:
        domain = urlparse("http://" + url).netloc

    # Remove "www." if present and split by ".".
    domain_parts = domain.split('.')
    
    # If "www" is present, return the next part, else return the first part.
    if domain_parts[0] == "www":
        return domain_parts[1]
    return domain_parts[0]
