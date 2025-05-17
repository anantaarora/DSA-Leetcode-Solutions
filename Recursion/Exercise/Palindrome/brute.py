import re

def isPalindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

isPalindrome("A man a plan a canal: Panama") # True