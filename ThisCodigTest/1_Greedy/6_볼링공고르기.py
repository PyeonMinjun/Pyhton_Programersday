n,m= map(int,input().split())
ns = list(map(int,input().split()))

ns.sort()

target = 1 
cnt = 0 

for i in range(n-1):
    for j in ns:
        if ns[i] < j:
            cnt += 1
            
        
print(cnt)
    
    
    
    

