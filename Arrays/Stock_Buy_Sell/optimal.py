
def stock_buy_sell(arr):
    n = len(arr)
    max_profit = 0
    min_price = float('inf')
    for i in range(0, n):
        min_price = min(min_price, arr[i])
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)

print(stock_buy_sell([7,1,5,3,6,4])) # 5