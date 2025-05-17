# Wrong approach: as it will return 1 as soon as it finds a sorted pair eg: [45444]
# we should give the condition which will fail and return 0

# def isSorted(n: int,  a: [int]) -> int:
#     for i in range(0,len(a)-1):
#         if a[i] <= a[i+1]:
#             return 1
#     return 0

# Correct approach
def isSorted(n: int,  a: [int]) -> int:
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            return 0
    return 1

arr = [1,2,3,4,5]
print(isSorted(len(arr),arr)) # 1