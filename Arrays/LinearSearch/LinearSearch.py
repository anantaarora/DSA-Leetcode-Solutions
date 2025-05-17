def searchInSorted(arr, N, K):
    
    for i in range(N):
        if arr[i] == K:
            return 1
    return -1

# Time Complexity: O(N)
# Space Complexity: O(1)

arr = [1,2,3,4,5], N = 5, K = 4
print(searchInSorted(arr, N, K)) # 1
