# Logic: Either we can do using sets or dictionary
# Sets will not preserve the order so No
# Dictionary will preserve the order so Yes

# condition: you have to do inplace changes that means you need to change the original array and 
# not create a new array

def removeDuplicates(arr):
    my_dict = {}
    for i in range(len(arr)):
        my_dict[arr[i]] = 0
    j = 0
    for key in my_dict:
        arr[j] = key
        j += 1
    return j

arr = [1,2,2,3,4,4,4,5]
print(removeDuplicates(arr))

