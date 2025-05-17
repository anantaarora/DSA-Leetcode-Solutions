

def majority_element(nums):
    result = {}
    for nums in nums:
        result[nums] = result.get(nums, 0) + 1
    for key, value in result.items():
        if value > len(nums) // 2:
            return key
    return -1

print(majority_element([2,2,1,1,1,2,2])) # 2
