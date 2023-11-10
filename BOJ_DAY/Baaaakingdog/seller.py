t = int(input())

for tc in range(1,t+1):
    n = int(input())
    
    stk = []
    res = 0
    total = 0
    
    for _ in range(n):
        ns = list(map(int,input().split()))
        if ns[0] == 1:
            if stk:
                if ns[1] > stk[0]:
                    stk[0] = ns[1]
            else:
                stk.append(ns[1])
        
        else:
            if stk:
                if stk[0] == ns[1]:
                    res = stk.pop()
                else:
                    continue
            else:
                continue
    
    print("#""{} {}" .format(tc,res) )
                
                

    
            
    
    
    
    

