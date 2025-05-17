
import re

def isPalindrome(s: str, start = 0) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if start > len(s)//2:
        return True
    if s[start] != s[len(s) - start - 1]:
        return False
    return isPalindrome(s, start + 1)

print(isPalindrome("A man a plan a canal: Panama"))# True
