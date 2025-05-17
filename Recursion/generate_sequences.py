

def backtrack(subset, index, nums):

    if index >= len(nums):
        result.append(subset.copy())
        return
    
    subset.append(nums[index])
    backtrack(subset, index + 1, nums) # include the current number
    subset.pop() # backtrack
    backtrack(subset, index + 1, nums) # exclude the current number





result = []
nums = [3, 1, 2]
backtrack([], 0, nums) # we are starting with 0th index
print(result)