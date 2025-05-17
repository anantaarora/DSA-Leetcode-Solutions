from math import sqrt
# Tc: O(n), Sc: O(1)

def sumOfAllDivisors(n: int) -> int:
    sum  = 0
    for i in range(1, n+1):
        sum += i*(n//i)
    return sum 

digit = int(input("Enter number: "))
print(sumOfAllDivisors(digit))