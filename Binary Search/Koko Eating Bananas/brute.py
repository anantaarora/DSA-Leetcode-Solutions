import math

def koko_bananas(total_piles, hourly_rate):
    totalB = 0
    for i in range(len(total_piles)):
        totalB = totalB + math.ceil(total_piles[i] / hourly_rate)

    return totalB


total_piles = [3,6,7,11]
min_rate = 1
max_rate = max(total_piles)
for i in range(min_rate, max_rate+1):
    th = koko_bananas(total_piles, i)
    if th <= 8:
        print(i)
        break