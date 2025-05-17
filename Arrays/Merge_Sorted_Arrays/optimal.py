def mergesorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

    # what is one of them exhausts first
    while i < len(arr1):
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

arr1 = [1, 1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6]

print(mergesorted(arr1, arr2)) # [1, 2, 3, 4, 5, 6]
# Time complexity: O(n+m) where n and m are the lengths of the two arrays
# Space complexity: O(n+m) where n and m are the lengths of the two arrays