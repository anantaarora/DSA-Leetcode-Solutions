# TC: O(n x sqrt(n))
# SC: O(N)

from math import sqrt

def sumOfAllDivisors(n: int) -> int:
    sum  = 0
    for num in range(1, n+1):
        for i in range(1, int(sqrt(num))+1):
            if num % i == 0:
                sum += i
            if num//i != i:
                sum += num//i
    return sum 

digit = int(input("Enter number: "))
print(sumOfAllDivisors(digit))