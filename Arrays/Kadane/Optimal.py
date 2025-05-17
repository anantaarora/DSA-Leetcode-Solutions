## Maximum Subarray
def maxSubArraySum(arr):
    maxi = float('-inf')
    sum = 0
    n = len(arr)
    for i in range(n):
        sum += arr[i]
        if sum > 0:
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi

print(maxSubArraySum([-2,1])) # 1
    