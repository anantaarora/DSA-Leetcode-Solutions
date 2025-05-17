


def singlelement(arr):
    temp = {}
    for i in arr:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    for i in temp:
        if temp[i] == 1:
            return i
    return -1

arr = [1,1,2,3,3,4,4,8,8]
print(singlelement(arr))