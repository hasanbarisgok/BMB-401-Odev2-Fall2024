'''
Created on Oct 18, 2024
Modified on Nov 7, 2024

@author: Hasan Baris GOK
'''

def paraBozdur(miktar):

    # If the input value is not valid, returns an empty list.
    if not isinstance(miktar, (int, float)) or miktar <= 0 or miktar >= 100:
        return []

    # Banknotes ve coin values (USD, and Cent)
    denominations = [20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    counts = [0] * 8  # Create an list with 8 elements.

    # Requesting the remaining amounts.
    remaining = round(miktar, 2)  # Rounding for fractional amounts

    for i, denom in enumerate(denominations):
        if remaining >= denom:
            counts[i] = int(remaining // denom)  # How many of this banknote/coin can be used?
            remaining = round(remaining - counts[i] * denom, 2)  # Update remaining amount

    return counts
