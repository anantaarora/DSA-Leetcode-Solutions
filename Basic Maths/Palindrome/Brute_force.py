def reverse(num: int) -> int:
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result*10) + last_digit
        n = n // 10
    return result

def checkPalindrome(num : int) -> bool:
        reversed : int = reverse(num)
        if num == reversed:
            return True
        else: 
            return False
        
n =int(input("Enter a number:"))
print(checkPalindrome(n))