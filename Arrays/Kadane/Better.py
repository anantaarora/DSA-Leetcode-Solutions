from typing import List

def maxSubArray(nums: List[int]) -> float:
    maxi = float("-inf")
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):

            # add the current element arr[j]
            # to the sum i.e. sum of arr[i...j-1]
            sum += nums[j]

            maxi = max(maxi, sum)  # getting the maximum
    return maxi

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6