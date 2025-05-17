# Recusrion to reverse an array

def reverse(arr, start, stop):
    if start > stop:
        return arr
    while start<stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        return reverse(arr, start+1, stop-1)