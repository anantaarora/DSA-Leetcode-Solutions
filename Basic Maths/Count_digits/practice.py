

# 1. brute force approach
digits = int(input("Enter number of digits:"))
print(f"Number of digits: {len(str(digits))}")

# 2. Better approach: for loop is not a good approach as you have to convert to string
# TC is O(n+n) = O(2n)
def countDigits2(n: int) -> int:
    count  = 0
    length = len(str(n))
    for i in range(0, length):
        count += 1
    return count

print(countDigits2(digits))

# 3. Better approach using while loop -> O(logn)
def countDigits3(n: int) -> int:
    count  = 0
    while n > 0:
        n = n//10
        count += 1
    return count

print(countDigits3(digits))

# 4. Optimal approach
import math

def countDigits4(n: int) -> int:
    return int(math.log10(n))+1

print(countDigits4(digits))

