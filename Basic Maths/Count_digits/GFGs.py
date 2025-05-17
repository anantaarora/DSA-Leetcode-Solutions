# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.


def evenlyDivides (N):
    original = N
    count = 0
    while N>0:
        digit = N%10
        if digit>0 and original%digit == 0:
            count+= 1
            print("digit",digit)
        N =N//10
      
    return count

print(evenlyDivides(22074))