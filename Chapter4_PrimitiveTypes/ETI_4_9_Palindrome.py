import math


def is_palindrome_number(x: int) -> bool:
    """
    All negative numbers are not palindromes.
    :param x: integer
    :return: True if x is a palindrome in decimal system
    """
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log(10)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask  # Remove the MSD
        x //= 10  # Remove the LSD
        msd_mask /= 100

    return True