
def missingNumber(arr):
    n = len(arr)
    for i in range(n+1):
        if i not in arr:
            return i

arr = [0, 1, 2, 3, 4, 5, 6, 7, 9]
print(missingNumber(arr)) # 8

# Time complexity: O(n^2) because for loop  takes O(N) and in operator take O(n) so O(n^2)
# Space complexity: O(1) because we are not using any extra space
    
