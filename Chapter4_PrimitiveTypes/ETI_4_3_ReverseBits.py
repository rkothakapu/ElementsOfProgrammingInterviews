from Chapter4_PrimitiveTypes.ETI_4_2_SwapBits import swap_bits


def reverse_bits(x: int) -> int:
    """
    If we need to perform this operation just once, there is a simple brute-force algorithm
    :param x: 64-bit unsigned integer
    :return: integer with bits reversed in input
    """
    i = 0
    j = 63
    while i < j:
        x = swap_bits(x, i, j)
        i += 1
        j -= 1

    return x


def reverse_bits_with_cache(x: int) -> int:
    """" To implement reverse when the operation is to be performed repeatedly, we look more carefully at the
    structure of the input, with an eye towards using a cache.
    :param x: 64-bit unsigned integer
    :return: integer with bits reversed in input
    """
    mask_size = 16
    bit_mask = 0xFFFF
    PRECOMPUTED_REVERSE = {}  # Let this holds valid precomputed reverse bit for all possible 16 bit word
    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) |
            PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size) |
            PRECOMPUTED_REVERSE[x >> (2 * mask_size) & bit_mask] << mask_size |
            PRECOMPUTED_REVERSE[x >> (3 * mask_size) & bit_mask])