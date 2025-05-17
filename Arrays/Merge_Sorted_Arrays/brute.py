def findUnion(arr1,arr2,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    freq = set()
    for i in range(len(arr1)):
        freq.add(arr1[i])
    for j in range(len(arr2)):
        freq.add(arr2[j])
        
    return sorted(list(freq))

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]
print(findUnion(arr1, arr2, 5, 5)) # [1, 2, 3, 4, 5, 6, 7]