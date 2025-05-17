

def min_rotated_sorted(arr):
    n = len(arr)
    minimum = float('inf')
    for i in range(0, n):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

# Time complexity: O(n)
# Space complexity: O(1)