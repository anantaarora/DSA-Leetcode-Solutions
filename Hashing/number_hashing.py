arr = [5,8,3,1,5,11,3,8,7,6,5]
n = len(arr)
hash = [0]*12

#updating the hash table
for i in range(n):
    hash[arr[i]] += 1

#searching the element in the hash table
num = int(input("enter the number to search: "))
print(hash[num])

#Time complexity: O(m+n)
## Drawback: if aray size is big then it will take more time.