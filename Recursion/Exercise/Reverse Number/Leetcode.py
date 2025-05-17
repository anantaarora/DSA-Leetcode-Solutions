def reverse(x: int) -> int:
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
        if rev < (-2**31) or rev > (2**31-1):
            return 0
        return rev

num = 123
print(reverse(num)) 