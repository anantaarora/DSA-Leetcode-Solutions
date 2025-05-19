# Print GFG n times without the loop.

def printGfg(n):
    if n>0:
        printGfg(n-1)
        print("GFG", end =" ")

printGfg(5) # GFG GFG GFG GFG GFG