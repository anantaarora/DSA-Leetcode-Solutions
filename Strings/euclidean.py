
import math

def euclidean(arr):
    n = len(arr)
    minimum = float('inf')
    for i in range(0, n):
        distance = math.sqrt(arr[i][0]**2 + arr[i][1]**2)
        if distance < minimum:
            minimum = distance
            pair = [arr[i][0], arr[i][1]]
    return pair

print(euclidean([[1,2], [3,4], [5,6], [7,8]])) # [1, 2]
            