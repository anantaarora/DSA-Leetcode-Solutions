def isPalindrome(x):
    rev = 0
    num = x
    is_negative = False
    if x<0:
        is_negative = True
        x = abs(x)
    while x > 0:
        ld = x%10
        rev = rev * 10+ ld
        x = x //10
    if is_negative:
        rev = rev * -1
    if str(rev) == str(num):
        return True 
    return False

digit = int(input("Enter number:"))
print(isPalindrome(digit))
       