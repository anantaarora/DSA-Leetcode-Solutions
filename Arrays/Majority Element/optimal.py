# Moores Voting Algorithm

from typing import List

def majorityElement( nums: List[int]) -> int:
    candidate = nums[0]
    count = 0
    for i in range(len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = nums[i]
    return candidate

print(majorityElement([2,2,1,1,1,2,2])) # 2