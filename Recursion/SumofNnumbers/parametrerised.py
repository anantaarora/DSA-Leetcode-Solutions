
def recursive(n: int, sums: int):
    if n < 1:
        return
    recursive(n-1, sums + n)
    return sums 


def sumFirstN(n: int) -> int:
    sums = 0
    sums = recursive(n, sums)
    return sums

print(sumFirstN(5)) 