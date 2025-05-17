
def rotate(arr,k):
    rotations = k % len(arr)
    for i in range(rotations):
        last = arr.pop()
        arr.insert(0, last)
    return arr

arr = [1,2,3,4,5,6,7]
k = 3
print(rotate(arr, k)) # [5, 6, 7, 1, 2, 3, 4]
