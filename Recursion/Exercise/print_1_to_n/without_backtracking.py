# Solution: Without Back tracking
# Time complexity is O( n ).

from typing import List
def recursive(n: int, x : int, result: List[int]) -> None:
    if x > n:
        return
    result.append(x)    
    recursive(n, x+1, result)
    
     

def printNos(n: int) -> List[int]: 
    result = []
    x = 1
    recursive(n, x, result)
    return result

print(printNos(5))