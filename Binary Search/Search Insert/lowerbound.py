

def lowerbound(arr, target):
    low = 0 
    lb = len(arr)
    high = len(arr)-1
    while low <= high:
        mid = (low +high)//2
        if arr[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb


print(lowerbound([1,2,4,4,4,4,6,6,6,6,8,9,9,10], 4)) # 4