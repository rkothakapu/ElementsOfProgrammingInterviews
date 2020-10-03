def power(x: float, y: int) -> float:
    """
    :param x: a double
    :param y: integer
    :return: x ** y
    """
    result = 1
    if y < 0:
        x, y = 1.0 / x, -y
    while y:
        if y & 1:
            result *= x
        x, y = x * x, y >> 1
    return result