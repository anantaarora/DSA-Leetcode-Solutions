

def armstrong(n):
    num = n
    total = 0
    nod = len(str(n))
    while n>0:
        ld = n%10
        total += ld**nod
        n = n//10
    return total == num

armstrong(153) # True
