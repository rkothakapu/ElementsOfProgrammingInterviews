def parity(x: int) -> int:
    """
    The parity of a binary word is 1 if the number of 1s in the word is odd
    Otherwise, it is 0
    :param x: word
    :return: 1 if # of 1 bits is odd, else 0
    """
    # brute force
    # O(n)
    result: int = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity2(x: int) -> int:
    """
    The parity of a binary word is 1 if the number of 1s in the word is odd
    Otherwise, it is 0
    :param x: word
    :return: 1 if # of 1 bits is odd, else 0
    """
    # find the next Least Significant 1 bit
    # O(k) k - # of 1 bits
    result = 0
    while x:
        x &= x-1
        result ^= 1
    return result


def parity3(x: int) -> int:
    """
    The parity of a binary word is 1 if the number of 1s in the word is odd
    Otherwise, it is 0
    :param x: 64-bit word
    :return: 1 if # of 1 bits is odd, else 0
    """
    # Using cache
    # O(n/L) - L is the size of the mask
    PRECOMPUTED_PARITY = {}
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
            PRECOMPUTED_PARITY[(x >> (2 * mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^
            PRECOMPUTED_PARITY[x & bit_mask])


def parity4(x: int) -> int:
    """
    The parity of a binary word is 1 if the number of 1s in the word is odd
    Otherwise, it is 0
    :param x: word
    :return: 1 if # of 1 bits is odd, else 0
    """
    # In the brute-force, we basically performed b0 ^ b1 ^ b2 ^ ....
    # which would be same as (b0b1b2b3) ^ (b4b5b6b7) ^ ...
    # and then recursively (c0c1) ^ (c2c3), d0 ^ d1
    # Complexity - O(log n)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
