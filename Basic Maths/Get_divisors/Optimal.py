from typing import List

def getAllDivisors(n: int) -> List[int]:
    result  = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            if n//i != i:
                result.append(n//i) 
    result.sort()                 
    return result 

digit = int(input("Enter number: "))
print(getAllDivisors(digit))


def sumOfAllDivisors(n: int) -> int:
    result  = 0
    print(int(n**0.5))
    for i in range(1, int(n**0.5)+1):
        total = 0
        if n % i == 0:
            total += i
            if n//i != i:
                total += n//i
        print(total)
        result += total
    return result 

digit = int(input("Enter number: "))
print(sumOfAllDivisors(digit))