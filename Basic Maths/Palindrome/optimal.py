def isPalindrome(x: int) -> bool:
    rev = 0
    is_negative = False
    num = x
    if x<0:
        is_negative = True
        x = abs(x)
    while x > 0:
        ld = x%10
        rev = rev * 10+ ld
        x = x //10
    if is_negative:
        rev = str(rev) + "-" 
    # if str(rev) == str(num):
    #     return True 
    return str(rev) == str(num)

digit = int(input("Enter number:"))
print(isPalindrome(digit))
        