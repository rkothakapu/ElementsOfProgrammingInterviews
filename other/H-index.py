from typing import List


def h_index(arr: List[int]) -> int:
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= len(arr) - i:
            return len(arr) - i

    return 0


if __name__ == "__main__":
    print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))
