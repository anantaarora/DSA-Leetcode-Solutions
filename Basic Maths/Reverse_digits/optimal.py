# Optimal solution
# TC: O(log(n))
# SC: O(1)

def reverse_digits(x: int) ->int:
    rev = 0
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)
    while x > 0:
        ld = x % 10
        rev = rev*10 + ld 
        x = x//10
    if is_negative:
        rev = rev * -1
    if (rev < -2**31) and (rev > 2**31-1):
        return 0
    return rev

n = int(input("Enter number:"))
print(reverse_digits(n))

# or 2nd solution:

def reverse_digits(x: int) ->int:
    rev = 0
    is_negative =1
    if x < 0:
        is_negative = -1
        x = abs(x)
    while x > 0:
        ld = x % 10
        rev = rev*10 + ld 
        x = x//10
    rev = rev * is_negative
    if (rev < -2**31) or (rev > 2**31-1):
        return 0
    return rev
