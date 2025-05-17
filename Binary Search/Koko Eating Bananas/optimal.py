import math

def koko_bananas(total_piles, hourly_rate):
    totalB = 0
    for i in range(len(total_piles)):
        totalB = totalB + math.ceil(total_piles[i] / hourly_rate)

    return totalB


def bananas(total_piles, low, high):
    while low <= high:
        mid = (low + high) // 2
        th = koko_bananas(total_piles, mid)
        if th <= 8:
            high = mid - 1
        else:
            low = mid + 1
        
    return low

total_piles = [3,6,7,11]
low = 1
high = max(total_piles)