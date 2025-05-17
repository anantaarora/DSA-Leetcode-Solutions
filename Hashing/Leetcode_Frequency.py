
# Hint: we will solve this question later as it requires sliding window

def maxFrequency(nums, k: int) -> int:
    hash_list = {}
    max_num = max(nums)
    for i in nums:
        hash_list[i] = max_num - i
    return max(hash_list.values())

lst = [1,2,4]
print(maxFrequency(lst, 5)) # 3