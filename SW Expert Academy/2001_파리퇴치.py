t = int(input())


for cnt in range(1,t+1):
    N,M= map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dietotal = []
    
    for i in range(N-M+1): # 0
        for j in range(N-M+1): # 0,1,2,3
            total = 0
            for ci in range(M): # 0, 1
                for cj in range(M):# 0 ,1
                    if i + ci in range(N) and j + cj in range(N):
                        total += arr[i+ci][j+cj]
            dietotal.append(total)
            
            
    print("#{} {}" .format(cnt, max(dietotal)))