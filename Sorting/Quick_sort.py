"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex < endIndex:
        p_index = partition(arr, startIndex, endIndex)
        quickSort(arr, startIndex, p_index - 1)
        quickSort(arr, p_index + 1, endIndex)


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


