# Implement Fibonacci series 
# If  n == 0 or n == 1, return n

def fibo(n: int):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(5)) # 8