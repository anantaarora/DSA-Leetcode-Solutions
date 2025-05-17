

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




def min_days(bloom_day, low, high):
    while low <=  high:
        mid = (low + high) // 2
        poss = bloom_d(bloom_day, 2, 3, mid)
        if poss:
            high = mid - 1
        else:
            low = mid + 1
    
    return low # remember we are returning low here, returning mid would be wrong

bloom_day = [7,7,7,7,13,11,12,7]
low = min(bloom_day)
high = max(bloom_day)
print(min_days(bloom_day, low, high)) # 11

