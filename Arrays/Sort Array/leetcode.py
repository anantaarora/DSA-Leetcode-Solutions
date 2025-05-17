from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        rotations = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] > nums[(i+1)%n]:
                rotations += 1
                if rotations >1:
                    return False
        return True