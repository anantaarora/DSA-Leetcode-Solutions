# Print N to 1 using Recursion without Backtracking

def func1(n):
    if n<1:
        return
    print(n)
    func1(n-1)

func1(5)

def func2(i,n):
    if i>n:
        return
    print(n)
    func2(i,n-1)

func2(1,5)


def func3(i,n):
    if i>n:
        return
    print(n-i+1)
    func3(i+1,n)

func3(1,5)
