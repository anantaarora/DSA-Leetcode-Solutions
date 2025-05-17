
# Create flow
# Base case
# Fact(0) pr Fact(1) == 1

def factorial(n: int)-> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number:"))
print(factorial(n))