

def upperbound(arr, target):
    low = 0 
    ub = len(arr)
    high = len(arr)-1
    while low <= high:
        mid = (low +high)//2
        if arr[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub


print(upperbound([1,2,4,4,4,4,4,4,4,4,8,9,9,10], 4)) # 4