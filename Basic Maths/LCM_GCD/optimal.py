# Using Euclidean Algorithm



def gcd_eud(a, b) -> tuple[int,int]:
    def gcd(a,b):
        while b:
            a, b = b, a % b
        return a

    gcd_value = gcd(a, b)
    
    # LCM calculation using (A * B) // GCD
    lcm_value = (a*b) // gcd_value
    
    return int(lcm_value), gcd_value


print(gcd_eud(5, 10)) # 10, 5

## recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)