def reverse(arr, start, stop):
    if start > stop:
        return arr
    while start<stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        return reverse(arr, start+1, stop-1)


def rotate(arr,k):
    l = len(arr)
    reverse(arr, l-k, l-1) 
    reverse(arr, 0, l-k-1) 
    reverse(arr, 0, l-1) 
    return arr

arr = [1,2,3,4,5,6,7]
k = 3
print(rotate(arr, k)) # [5, 6, 7, 1, 2, 3, 4]