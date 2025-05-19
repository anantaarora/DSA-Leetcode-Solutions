# Print numbers from N to 1 (space separated) without the help of loops.

def printNos(n):
    if n >0:
        print(n, end=' ')
        printNos(n-1)

printNos(5) # 5 4 3 2 1 0