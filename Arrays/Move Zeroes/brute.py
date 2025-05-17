def moveZeros(n: int,  a: [int]) -> [int]:
    i = 0
    while i < n-1:
        if a[0] == 0:
            element = a.pop(0)
            print(element)
            a.insert(n-1, element)
            print(a)
            i = i+1

    return a

n = 5
a = [0,0,0,1]
b= [4,0,3,2,5]
print(moveZeros(n, b)) # [1, 0, 0, 0]