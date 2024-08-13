t = int(input())

for _ in range(t):
    n = int(input())
    ns = list(map(int,input().split()))[::-1]
    
    k = ns[0]
    res = 0
    for i in ns[1:]:
        if i > k:
            k = i
        elif i < k:
            res += k-i
            
            
    print(res)    
        
        
    
    
    
    
    