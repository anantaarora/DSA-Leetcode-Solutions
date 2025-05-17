def factorialNumbers(n, i=1, fact=1, result=None):
    if result is None:
        result = []
    
    if fact > n:
        return result
    
    result.append(fact)
    return factorialNumbers(n, i + 1, fact * (i + 1), result)


print(factorialNumbers(120)) # [1, 2, 6, 24, 120]