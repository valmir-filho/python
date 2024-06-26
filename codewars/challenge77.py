"""
Create a function that converts US dollars (USD) to Chinese Yuan (CNY).
The input is the amount of USD as an integer, and the output should be a
string that states the amount of Yuan followed by "Chinese Yuan"
"""


def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"
  
