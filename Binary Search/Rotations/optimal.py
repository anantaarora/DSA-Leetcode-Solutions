


def k_rotations(arr):
    n = len(arr)
    low = 0
    high = n - 1
    minimum = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        if arr[low] <= arr[high]:
            minimum = arr[low]
            index = low
        if arr[low] < arr[mid]:
            minimum = min(minimum, arr[low])
            index = low
            low = mid + 1
        else:
            minimum = min(minimum, arr[mid])
            index = mid
            high = mid - 1
    return index

# Time complexity: O(log(n))
# Space complexity: O(1)

print(k_rotations([4,5,6,7,0,1,2])) # 4
