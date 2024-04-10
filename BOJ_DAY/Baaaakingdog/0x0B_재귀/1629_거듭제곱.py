def func1(a,b,m):
    if b == 1:
        return a % m
    
    val = pow(a, b//2, m)
    
    val = (val * val) % m
    
    if (b%2 == 0):
        return val
    return val * a % m


a,b,c = list(map(int,input().split()))
print(func1(a,b,c))