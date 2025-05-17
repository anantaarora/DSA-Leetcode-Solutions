# Using only one index 
# n//2 because we will run the loop till half of the array

def revAr(arr, ind):
    n = len(arr)
    if ind == n //2:
        print(arr)
        return
    arr[ind], arr[n-ind-1] = arr[n-ind-1], arr[ind]
    revAr(arr, ind+1)

arr = [1,2,3,4,5]
revAr(arr, 0)