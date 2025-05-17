

def longest_subarray(arr, target):
    n = len(arr)
    max_len = 0
    s = 0
    sum_map = dict()
    for i in range(0,n):
        s += arr[i]
        if s == target:
            max_len = i+1
        remaining = s - target
        if remaining in sum_map:
            max_len = max(max_len, i-sum_map[remaining])
        if s not in sum_map:
            sum_map[s] = i

    return max_len


print(longest_subarray([1, 1, 1, 1, 0, 0, 1, 0, 1], 2))