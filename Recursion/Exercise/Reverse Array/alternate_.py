# Using only one index 
# n//2 because we will run the loop till half of the array

def revAr(arr, ind):
    n = len(arr)
    if ind == n //2:
        print(arr)
        return
    arr[ind], arr[n-1-ind] = arr[n-1-ind], arr[ind]
    revAr(arr, ind+1)