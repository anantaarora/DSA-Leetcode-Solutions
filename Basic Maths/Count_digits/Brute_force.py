# 3. Better approach using while loop -> O(logn)
def countDigits3(n: int) -> int:
    count  = 0
    while n > 0:
        n = n//10
        count += 1
    return count


digits = int(input("Enter number of digits:"))
print(countDigits3(digits))