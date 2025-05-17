# Brute force solution using slicing
def palindrome(s):
    return s == s[::-1]

s = input("Enter string:")
print(palindrome(s))


# Alternate optimal solution using recursion one pointer
def ispalindrome(s, i=0):
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-1-i]:
        return False
    return ispalindrome(s, i+1)

s = input("Enter string:")
print(ispalindrome(s))