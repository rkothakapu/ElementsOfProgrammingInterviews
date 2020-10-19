from typing import List


def rearrange(A: List[int]) -> None:
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i % 2))


if __name__ == '__main__':
    A = [1, 10, 22, 11, 13, 5, 4, 2, 5, 6]
    rearrange(A)
    print(A)