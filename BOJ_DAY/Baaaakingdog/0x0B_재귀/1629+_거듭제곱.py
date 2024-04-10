#1제곱을 구할 수 있디.
#k승을 계산했으면 2k승과 2k+1승도 구할 수 있다.

#-> 귀납적으로 해결

def func1(a,b,m):
    
    if b == 1:
        return a % m
    
    val = pow(a, b//2, m)
    val = (val * val) % m
     
    if b % 2 == 0:
        return val
    return val * a % m

a,b,m = map(int,input().split())
print(func1(a,b,m))
    
    
    
    
    
    