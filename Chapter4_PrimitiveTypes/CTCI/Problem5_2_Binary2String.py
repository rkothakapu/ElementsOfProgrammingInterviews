def binary2String(num):
    """
    Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation.
    If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".
    :param num: real number between 0 and 1
    :return: binary representation string
    """
    if num <= 0 or num >= 1:
        return "Error"

    binary = ['.']
    frac = 0.5
    while num > 0:
        if len(binary) >= 32:
            return "Error"
        if num >= frac:
            binary.append('1')
            num -= frac
        else:
            binary.append('0')

        frac /= 2

    return ''.join(binary)


if __name__ == "__main__":
    print(0.625, binary2String(0.625))