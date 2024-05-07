t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    nss = list(map(int,input().split()))
    
    arr = []
    enm = []
    
    for i,nx in enumerate(nss): 
        enm.append((nx,i+1)) 
    
    k = enm[m][1]
    
    
    while enm:
        for i in range(1,len(enm)):
            if enm[0][0] < enm[i][0]:
                enm.append(enm.pop(0))
                break
        else:    
            arr.append(enm.pop(0))
    
    cnt = 0
    for x,y in arr:
        cnt += 1
        if y == k:
            break
    print(cnt)
            
        
    
        

    
    
    