t = int(input())

for tc in range(1,t+1):
    arr = [0] * 101
    
    
    n = int(input())
    ns = list(map(int,input().split()))
    
    cnt = 0
    res = 0
    
    
    for i in ns:
        arr[i] += 1
        
        if arr[i] > cnt:
            cnt = arr[i]
            res = i
        elif arr[i] == cnt:
            if i > res:
                res = i
    print(res)
  
   