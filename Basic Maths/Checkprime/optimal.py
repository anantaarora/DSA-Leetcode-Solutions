# Time complexity: O(n/2) ~O(n)
# Space complexity: O(1) because the size is not increasing /decreasing of any variable

def isprime(n : int)-> bool:
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
isprime(n)

# or Method 2:
n = int(input())
if n == 1:
    print("NO")

else:
    for i in range(2, int(n**0.5)+1):
        if n% i == 0:
            print("NO")
            break
        else:
            print("YES")