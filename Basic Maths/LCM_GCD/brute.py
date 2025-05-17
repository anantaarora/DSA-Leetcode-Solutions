# LCM and GCD of two numbers

import math

def lcmAndGcd( A , B):
    if A> B:
        small = B
    else:
        small = A
    for i in range(1, small+1):
        if((A % i == 0) and (B % i == 0)):
            gcd = i
    return int(A*B/gcd), gcd

print(lcmAndGcd(5, 10)) # 10, 5


