from typing import List

def maxSubArray(nums: List[int]) -> float:
    maxi = float("-inf")
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            summ = 0

            # add all the elements of subarray
            for k in range(i, j + 1):
                summ += nums[k]

            maxi = max(maxi, summ)
    return maxi

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6