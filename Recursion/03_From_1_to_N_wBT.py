# Print hello 5 times using recursion

def printx(i,n):
    if i>n:
        return
    print("hello")
    printx(i+1,n)

printx(1,5)

# Print numbers from 1 to 5 using recursion without back tracking

def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)

func(1,5)


# Print numbers from 5 to 1 using recursion without backtracking

def func(i,n):
    if i>n:
        return
    print(n)
    func(i,n-1)

func(1,5)


# or
def func(n):
    if 1>n:
        return
    print(n)
    func(n-1)

func(5)