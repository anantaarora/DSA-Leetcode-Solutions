def removeDuplicates(arr,n):
    result = []
    for i in range(0, n):
        if arr[i] not in result:
            result.append(arr[i])
    return len(result)

arr = [1,2,2,3,4,4,4,5]
print(removeDuplicates(arr,len(arr)))
