# def sumOfAllDivisors(n: int) -> int:
#     result  = 0
#     for i in range(1, n+1):
#         total = 0
#         for j in range(1, i+1):
#             if i % j == 0:
#                 total += j
#         result += total
#     return result 

# digit = int(input("Enter number: "))
# print(sumOfAllDivisors(digit))

# Optimal
# def sumOfAllDivisors(n: int) -> int:
#     result  = 0
#     print(int(n**0.5))
#     for i in range(1, int(n**0.5)+1):
#         total = 0
#         if n % i == 0:
#             if n//i != i:
#                 total += i
#                 total += n//i
#         print(total)
#         result += total
#     return result 

digit = int(input("Enter number: "))
print(sumOfAllDivisors(digit))