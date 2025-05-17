# Brute Force method to reverse the digits of a number

def reverse_digits(n:int) ->int:
    digits = str(n)
    return int(digits[::-1])

n = int(input("Enter number:"))
print(reverse_digits(n))