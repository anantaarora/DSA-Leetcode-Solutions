from typing import List

def backtrack(subset: List[int], index: int, total: int):
    if total  == k:
        result.append(subset.copy())
        return True
    
    elif total > k:
        return False
    
    if index >= len(nums):
        return False
    
    subset.append(nums[index])
    Sum = total + nums[index]
    pick = backtrack(subset, index + 1, Sum) # include the current number
    if pick == True:
        return True
    subset.pop()
    Sum = total
    backtrack(subset, index + 1, Sum) # exclude the current number





result = []
k = 50
nums = [10, 20, 30]
backtrack([], 0, 0) # we are starting with 0th index
print(result)