from typing import List

def backtrack(subset: List[int], index: int, total: int):
    if total  == k:
        result.append(subset.copy())
        return
    
    elif total > k:
        return
    
    if index >= len(nums):
        return
    
    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(subset, index + 1, Sum) # include the current number
    subset.pop()
    Sum = total
    subset.pop() # backtrack
    backtrack(subset, index + 1, Sum) # exclude the current number





result = []
k = 3
nums = [3, 1, 2]
backtrack([], 0, 0) # we are starting with 0th index
print(result)