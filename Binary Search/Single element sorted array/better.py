

def single_element(arr):
    n = len(arr)
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    for i in range(1, n-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]
    return -1

arr = [1,1,2,3,3,4,4,8,8]
print(single_element(arr))