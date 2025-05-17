

def pairWithMaxSum(arr, N): 
    maxSum = float('-inf')
  
    # Generate all subarrays of size >= 2 
    for i in range(N): 
        for j in range(i + 1, N): 
            # Calculate the sum of the smallest and second smallest elements 
            sum = arr[i] + arr[j] 
  
            # Check if the sum is greater than the current maximum sum 
            if sum > maxSum: 
                maxSum = sum
  
    return maxSum 
    

print(pairWithMaxSum([1, 2, 3, 4, 5], 5))  # 9
            