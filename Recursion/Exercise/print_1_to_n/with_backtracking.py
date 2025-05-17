# from typing import List

# def printNos(n: int) -> List[int]: 
#     result = []
#     x = 1
#     if n >= x :
#         result.append(x)
#         result.extend(printNos(x+1))
#     return result 


# ans = printNos(5)
# print(ans)


# Solution: With Back tracking
# Time complexity is O(n).
# Space complexity is  O(n)

from typing import List
def recursive(n: int, result: List[int]) -> None:
    if n == 0:
        return
    recursive(n-1, result)
    result.append(n)
     

def printNos(n: int) -> List[int]: 
    result = []
    recursive(n, result)
    return result

print(printNos(5))