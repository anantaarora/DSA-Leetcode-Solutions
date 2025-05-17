def traffic(n: int, m: int, vehicle: [int]) -> int:
    current_count = 0
    
    for num in vehicle:
        if num == 1:
            current_count += 1  
    print(current_count)
             
    return current_count +m 


print(traffic(25, 17, [1 ,0 ,1, 1 ,1 ,1, 1 ,0 ,1 ,0,1,1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0 ])) # 5