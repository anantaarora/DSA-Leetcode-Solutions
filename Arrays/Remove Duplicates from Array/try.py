def removedup(arr, n):
    for i in range(n-1, 0, -1):
        if arr[i] == arr[i-1]:
            arr.pop(i)
    return len(arr)

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(arr)
print(removedup(arr, n)) # 5