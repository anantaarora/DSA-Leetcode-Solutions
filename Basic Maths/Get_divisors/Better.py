# Dividing n by 2 because after that divisors are not there
# for eg: 100, 100/2 -> 50 and there is no divisor after 50
# Therefore, we can consider range until n/2+1

# Time complexity: O(n/2) ~O(n)
# Space complexity: O(1) because the size is not increasing /decreasing of any variable
# would be O(n) if we store all divisors in a list
# result list is answer to my first question.
# we are not adding it to space complexity

from typing import List

def getAllDivisors(n: int) -> List[int]:
    result  = []
    for i in range(1, n//2+1):
        if n % i == 0:
            result.append(i) # For divisors of 10, we have got[1, 2, 5]
    result.append(n) # we will append 10 explicitly
    return result 

digit = int(input("Enter number: "))
print(getAllDivisors(digit))


