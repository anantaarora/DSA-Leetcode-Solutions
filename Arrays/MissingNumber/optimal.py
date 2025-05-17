
def missingNumber(nums):
    n = len(nums)
    orig_sum = n * (n + 1) // 2
    return orig_sum - sum(nums)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 9]
print(missingNumber(arr)) # 8

# Time complexity: O(n) because we are iterating through the array once
# Space complexity: O(1) because we are not using any extra space