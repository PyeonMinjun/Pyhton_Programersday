t = int(input())

for _ in range(t):
    n = int(input())
    ns = list(map(int,input().split()))
    
    ns = reversed(ns)
    
    tmp = 0
    res = 0
    
    for i in ns:
        if i > tmp:
            tmp = i
        elif i <= tmp:
            res += tmp - i
            
    print(res)
            