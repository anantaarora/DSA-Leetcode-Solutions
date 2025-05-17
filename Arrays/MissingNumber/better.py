
def missingnum(arr):
    mydict = dict()
    n = len(arr)
    for i in range(0, n+1):
        mydict[i] = 0

    for num in arr:
        mydict[num] = 1

    for key, value in mydict.items():
        if value == 0:
            return key

arr = [0, 1, 2, 3, 4, 5, 6, 7, 9]
print(missingnum(arr)) # 8

# Time complexity: O(3n) because we are iterating through the array 3 times
# Space complexity: O(n) because we are using a dictionary to store the values