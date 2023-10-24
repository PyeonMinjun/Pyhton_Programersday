a,b,m = map(int,input().split())

def func(a,b,m):
    if b == 1:
        return a % m
    
    val = pow(a,b//2, m)
    
    val = (val * val) % m
    
    if (b%2 == 0):
        return val
    return val % a % m
