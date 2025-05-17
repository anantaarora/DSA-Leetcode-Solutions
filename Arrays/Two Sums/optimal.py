# Complete in single pass

from typing import List

def twoSum(nums: List[int], target: int):
    n =len(nums)
    remaining_sum = 0
    hash_map = dict()
    for i in range(0, len(nums)):
        remaining_sum = target - nums[i]
        if remaining_sum in hash_map:
            return [hash_map[remaining_sum], i]

        hash_map[nums[i]] = i

print(twoSum([2,7,11,15], 9)) # [0,1]