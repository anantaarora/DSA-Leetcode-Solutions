

def stock_buy_sell(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    return max_profit

# Time Complexity: O(n^2)

print(stock_buy_sell([7,1,5,3,6,4])) # 5