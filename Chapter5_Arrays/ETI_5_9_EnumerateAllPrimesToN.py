from typing import List
import math


def generate_primes(n: int) -> List[int]:
    """O(n sqrt(n))
    Hint: Exclude the multiples of prime
    :param n:
    :return:
    """
    if n < 2:
        return None

    primes = []
    for i in range(2, n+1):
        p = 0
        while p < len(primes) and primes[p] <= math.sqrt(i):
            if i % primes[p] == 0:
                break
            p += 1
        else:
            primes.append(i)

    return primes


def generate_primes2(n: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True] * n-1

    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2, n+1, p):
                is_prime[i] = False

    return False


if __name__ == '__main__':
    print(generate_primes(10))