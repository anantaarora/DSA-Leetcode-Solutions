
def frequencyCount(arr, N, P):
    P += 1
    for i in range(N):
        idx = arr[i] % P
        if idx <= N:
            arr[idx - 1] += P

    for i in range(N):
        arr[i] = arr[i] // P

arr = [2,3,3,2,5]
frequencyCount(arr, 5, 5)
print(arr)