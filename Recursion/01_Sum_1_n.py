def sum_func(i, sum=0):
    if i<1:
        print(sum)
        return
    sum_func(i-1, sum+i)

sum_func(5) # 15
