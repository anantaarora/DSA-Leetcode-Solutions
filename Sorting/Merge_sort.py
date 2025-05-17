def mergeSort(arr, l: int, r: int):
    m = (l + r) // 2

    # Sort first and second halves
    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)

    # Merge the sorted halves
    merge(arr, l, m, r)


def merge(arr, l,m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    merged = []
    i, j = 0, 0

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from left and right halves
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


arr = [64, 34, 25, 12]
sorted_arr = mergeSort(arr, l=0, r=0)
print(f"Sorted array = {sorted_arr}")