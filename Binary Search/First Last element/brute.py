

def first_last_element(arr, target):
    first = -1
    last = -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

print(first_last_element([1,2,4,4,4,4,6,6,6,6,8,9,9,10], 4)) # (2, 5)