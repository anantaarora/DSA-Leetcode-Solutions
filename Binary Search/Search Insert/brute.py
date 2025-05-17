

def binary_search(arr, target):

    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
       mid  = (low+high)//2
       if arr[mid] == target:
            return mid
       elif arr[mid] < target:
            low = mid+1
       else:
            high = mid-1
            
    return -1 # agar milta hi nahi hai toh -1 return karenge

print(binary_search([1,2,4,4,4,4,6,6,6,6,8,9,9,10], 4)) # 4

    