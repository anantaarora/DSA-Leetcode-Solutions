def rotateArray(arr: list, k: int) -> list:
    if k <1:
        return arr

    temp = arr[0]
    n  = len(arr)
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

    return rotateArray(arr, k-1)
