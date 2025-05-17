def rotate(arr,k):

    n = len(arr)
    rotations = k % n
    print(rotations)
    return arr[n-rotations:]+arr[:n-rotations] 
    # return arr[n-k:]+arr[:n-k] # wrong approach


arr = [1,2]
k = 5
print(rotate(arr, k)) # [5, 6, 7, 1, 2, 3, 4]