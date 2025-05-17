# Hint: Think of it as n = 1*2, 1*2*3 is nothing but n*3, 1*2*3*4 is nothing but n*4 and so on.
def factorialNumbers( n):
    result = []
    factorial = 1
    i = 1
    while factorial<=n:
        result.append(factorial)
        i +=1 
        factorial = factorial*i
    return result

print(factorialNumbers(120)) # [1, 2, 6, 24, 120]