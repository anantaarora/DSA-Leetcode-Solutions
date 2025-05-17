# Recusrion to reverse an array

def reverse(arr, start, stop):
    if start > stop:
        return arr

    arr[start], arr[stop] = arr[stop], arr[start]
    return reverse(arr, start+1, stop-1)
    
arr = [1, 2, 3, 4, 5]
print(reverse(arr, 2 , 4)) # [5, 4, 3, 2, 1]