
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    n = len(nums)
    while i<n:
        if nums[i] == 0:
            break
        i = i+1
    j = i+1
    while j<n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i = i+1
        j = j+1
    return nums

# Time Complexity: O(N)
# Space Complexity: O(1)

a = [0,0,0,1]
print(moveZeroes(a)) # [1, 0, 0, 0]
        