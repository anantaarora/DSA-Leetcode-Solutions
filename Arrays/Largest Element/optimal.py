from typing import List

def largestElement(arr: List, n: int) -> int:
    largest = arr[0]
    i = 0
    while i < n:
        if arr[i] > largest:
            largest = arr[i]
        i += 1
    return largest