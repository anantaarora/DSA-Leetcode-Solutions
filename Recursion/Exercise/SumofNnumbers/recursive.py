def sumFirstN(n: int) -> int:
    if n == 1:
        return 1
    return n + sumFirstN(n-1)

print(sumFirstN(5)) # 15