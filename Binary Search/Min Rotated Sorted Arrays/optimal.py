


def min_rotated_sorted(arr):
    n = len(arr)
    low = 0
    high = n - 1
    minimum = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        if arr[low] >= arr[high]:
            minimum = arr[low]
            break
        if arr[low] < arr[mid]:
            minimum = min(minimum, arr[low])
            low = mid + 1
        else:
            minimum = min(minimum, arr[mid])
            high = mid - 1
    return minimum

# Time complexity: O(log(n))
# Space complexity: O(1)
 