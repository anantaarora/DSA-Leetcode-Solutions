



def lower_bound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    lb = n # kyunki agar nahi mila toh length of the array
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid + 1
    return lb

def upper_bound(arr, target):   
    n = len(arr)
    low = 0
    high = n - 1
    ub = n # kyunki agar nahi mila toh length of the array
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid + 1
    return ub

def count_occurence(arr, target):
    n = len(arr)
    lb = lower_bound(arr, target)
    ub = upper_bound(arr, target)
    return ub - lb


print(count_occurence([1,2,3,3,3,3,5], 3)) # 4
