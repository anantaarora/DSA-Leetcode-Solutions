# Get all divisors of a number
# Sum of all divisors of a number

# Time complexity: O(n)
# Space complexity: O(1) because the size is not increasing /decreasing of any variable
# would be O(n) if we store all divisors in a list
# result list is answer to my first question.
# we are not adding it to space complexity

def getAllDivisors(n: int) -> list:
    result  = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result 

digit = int(input("Enter number: "))
print(getAllDivisors(digit))




# Time complexity: O(n * sqrt(n))

def sumOfAllDivisors(n: int) -> int:

    result  = 0
    for num in range(1, n+1):
        for i in range(1, int(num**0.5)+1):
            if n % i == 0:
                result += i
                if n//i != i:
                    result += n//i
    return result 

digit = int(input("Enter number: "))
print(sumOfAllDivisors(digit))
