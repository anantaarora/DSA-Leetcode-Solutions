## Count occurrences of a number in a sorted array with duplicates

def count_occurences(arr, target):
    count = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            count += 1
    return count


print(count_occurences([1,2,3,3,3,3,5], 3))