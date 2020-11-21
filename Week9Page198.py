from functools import reduce
def summation(lower, upper):
    """Returns the sum of the numbers from lower through upper."""
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x + y, range(lower, upper + 1))
