

def moveZeros(nums:[int]) -> [int]:
    temp = []
    for i in range(len(nums)):
        if nums[i] != 0:
            temp.append(nums[i])
    nz = len(temp)
    for i in range(0, nz):
        nums[i] = temp[i]
    for i in range(nz, len(nums)):
        nums[i] = 0
    return nums

# Time Complexity: O(N)
# Space Complexity: O(N) kyunki worst case mein temp array mein saare elements honge toh size of temp array inrease ho rha hai

a = [0,0,0,1]
print(moveZeros(a)) # [1, 0, 0, 0]