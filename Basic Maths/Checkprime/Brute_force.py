# Time complexity: O(n/2) ~O(n)
# Space complexity: O(1) because the size is not increasing /decreasing of any variable

def isprime(n : int)-> bool:
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

n = int(input())
isprime(n)