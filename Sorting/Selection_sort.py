from typing import List

def selectionSort(arr: List[int]) -> None: 
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] <arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
