### If only positive integers are allowed in the array then this is most optimal solution
## Using Two pointers approach

def longest_subarray(arr, k):

    n = len(arr)
    max_len = 0
    left = 0
    right = 0
    s = 0
    target = k
    while right <n:
        while left <= right and s > target:
            s -= arr[left]
            left += 1
        if s == target:
            max_len = max(max_len, right-left+1)
#  we are doing the below step because if right doesnt exhaust then only take sum
        right += 1
        if right < n:
            s += arr[right]

    return max_len

print(longest_subarray([1, 1, 1, 1, 0, 0, 1, 0, 1], 2)) # 5
# Time complexity: O(n)
# Space complexity: O(1)
    
