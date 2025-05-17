def reverseSubArray(arr,l,r):
    if l>r:
        return arr

    arr[l-1], arr[r-1] = arr[r-1], arr[l-1]
    return reverseSubArray(arr, l+1, r-1)

arr = [1, 2, 3, 4, 5]
print(reverseSubArray(arr, 2 , 4)) # [1, 4, 3, 2, 5]