

def longestsubarray(arr, k):
    n = len(arr)
    max_len = 0
    for i in range(n):
        s = 0 
        for j in range(i, n):
            s += arr[j]
            if s == k:
                max_len = max(max_len, j-i+1)
    return max_len

print(longestsubarray([1, 1, 1, 1, 0, 0, 1, 0, 1], 2)) # 5