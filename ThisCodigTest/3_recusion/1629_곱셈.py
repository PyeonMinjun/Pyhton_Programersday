def func1(a,b,m):
    if b == 1:
        return a % m
    
    val = func1(a,b//2,m)
    val = (val * val) % m
    
    if val % 2 == 0:
        return val
    return val * a % m
    
         
    
a,b,m = (map(int,input().split()))
print(func1(a,b,m))
