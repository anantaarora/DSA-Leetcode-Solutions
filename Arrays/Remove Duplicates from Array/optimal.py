def removeDuplicates(arr):
    i = 0
    j = i+1
    n = len(arr)

    # Base condition
    if n == 1:
        return 1
    while j <n:
        if arr[j] != arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i+1


arr = [1,2,2,3,4,4,4,5]
print(removeDuplicates(arr)) # 5