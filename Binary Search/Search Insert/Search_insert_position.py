# The below soltuins is same as lower bound because we need to find the index where the target should be inserted  return the index.
# If the target is not present in the array then return the index where it should be inserted.

def search(arr, target):
    n = len(arr)
    low = 0
    high = n-1
    index = len(arr)
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            index = mid
            high = mid-1
        else:
            low = mid+1
    return index

print(search([1,2,4,4,4,4,6,6,6,6,8,9,9,10], 4)) # 2