from typing import List
def recursive(n: int, result: List[str]) -> None:
    if n == 0:
        return
    recursive(n-1, result)
    result.append("Coding Ninjas")
     

def printNos(n: int) -> List[str]: 
    result = []
    recursive(n, result)
    return result

print(printNos(5))