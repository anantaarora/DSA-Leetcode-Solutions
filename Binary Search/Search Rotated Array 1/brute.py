

def search_rotated(arr, target):
    count = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i
    return -1


print(search_rotated([1,2,3,3,3,3,5], 3))