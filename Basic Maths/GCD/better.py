def calcGCD(n:int, m: int) -> int:
    result = []
    mul = m*n
    print(int(mul**0.5)+1)
    for i in range(1,int(mul**0.5)+1):
        if (m%i == 0) and (n%i == 0):
            result.append(i)
    return max(result)

result = calcGCD(4,6) 
print(result)