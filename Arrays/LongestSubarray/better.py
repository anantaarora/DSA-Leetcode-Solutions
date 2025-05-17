

def longestsubarray(arr, target):
    n = len(arr)
    max_len = 0
    for i in range(0,n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
            if s == target:
                max_len = max(max_len, j-i+1)
            if s > target:
                break
    return max_len

print(longestsubarray([1, 1, 1, 1, 0, 0, 1, 0, 1], 2)) # 5

# Time complexity: O(n^3)
# Space complexity: O(1)