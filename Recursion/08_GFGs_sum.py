def sumOfSeries(n):
    if n == 1:
        return 1
    else:
        return n**3 + sumOfSeries(n-1)
    
print(sumOfSeries(5))