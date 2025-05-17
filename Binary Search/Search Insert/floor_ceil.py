

def floor_ceil(arr, target):
    low = 0
    high = len(arr)-1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid, mid
        elif arr[mid] < target:
            floor = mid
            low = mid+1
        else:
            ceil = mid
            high = mid-1
    return floor, ceil


print(floor_ceil([1,2,4,4,4,4,6,6,6,6,8,9,9,10], 4)) # (4, 6)