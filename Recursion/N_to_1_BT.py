# Write a program to print numbers from N to 1 using Parameterized Recursion with Back tracking

def func(i, n):
    if i<1:
        return
    func(i-1,n)
    print(n-i+1)

func(5, 5)
