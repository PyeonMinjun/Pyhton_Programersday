T = int(input())

for tc in range(1,T+1):
    n,k = map(int,input().split())
    arr = []
    res = 0
    
    for i in range(n):
        arr.append(list(map(int,input().split())))

    for i in arr:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
            else:
                if cnt == k:
                    res += 1
                cnt = 0
                
        if cnt == k:
            res += 1 
            
    arr2 = list(zip(*arr))

    for i in arr2:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
            else:
                if cnt == k:
                    res += 1
                cnt = 0
                
        if cnt == k:
            res += 1 

    print("#{} {}" .format(tc, res))
