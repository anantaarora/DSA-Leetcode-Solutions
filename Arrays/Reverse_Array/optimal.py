def reverse(arr, start, stop):
    if start > stop:
        return arr
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse(arr, 0 , 4)) # [5, 4, 3, 2, 1]