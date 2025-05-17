



def search_rotated_array_1(arr, target):
    low= 0
    high = len(arr)-1
    n = len(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


print(search_rotated_array_1([8,9,1,2,3,4,5,6,7], 9)) 