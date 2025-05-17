# 4. Optimal approach
# Tc -> O(1)
# SC -> O(1)
import math

def countDigits4(n: int) -> int:
    return int(math.log10(n))+1


digits = int(input("Enter number of digits:"))
print(countDigits4(digits))