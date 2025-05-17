def pairWithMaxSum(arr, N):
    max_score = float('-inf')

    # Iterate over adjacent pairs to find the maximum sum
    for i in range(N - 1):
        # Calculate the sum of the current pair
        sum_pair = arr[i] + arr[i + 1]
        print(arr[i], arr[i + 1], sum_pair)
        # Update the maximum sum encountered
        max_score = max(max_score, sum_pair)

    return max_score

print(pairWithMaxSum([1, 2, 3, 4, 5], 5))  # 9