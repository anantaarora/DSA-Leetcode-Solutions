
def majorityElement(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count > len(nums) // 2:
            return nums[i]
    return -1

print(majorityElement([2,2,1,1,1,2,2])) # 2