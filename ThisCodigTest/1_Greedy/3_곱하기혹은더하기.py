N = input()
res =  0

for num in N:
    num = int(num)
    if num == 0 or num == 1 or res == 0:
        res += num
    
    else:
        res *= num
        
print(res)
    
    