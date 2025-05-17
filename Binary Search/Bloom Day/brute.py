

def bloom_d(bloomday, m, k, day):
    totalB = 0
    count = 0
    for i in range(len(bloomday)):
        if bloomday[i] <= day:
            count += 1
            if count == k:
                totalB += 1
                count = 0
        else:
            count = 0
    return totalB >= m


bloom_day = [7,7,7,7,13,11,12,7]
min_m = min(bloom_day)
max_m = max(bloom_day)
for i in range(min_m, max_m+1):
    if bloom_d(bloom_day, 2, 3, i):
        print(i)
        break
