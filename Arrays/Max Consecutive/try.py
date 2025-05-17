from typing import List


def findMaxConsecutiveOnes( nums: List[int]):
    i = 0
    count = 0
    max_count = 0
    while i < len(nums):
        if nums[i] == 1:
            count = 1
            j = i+1
            while j < len(nums) and nums[j] == 1:
                count += 1
                j += 1  
            i = j
            print(max_count, count)
            max_count = max(max_count, count)
        else:
            i += 1

        # print(result)
        # for i in range(len(result)):
        #     if result[i] > max:
        #         max = result[i]
    return max_count    
        
print(findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3