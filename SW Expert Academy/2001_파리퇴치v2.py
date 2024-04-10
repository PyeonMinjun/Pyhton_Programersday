t = int(input())


for cnt in range(1,t+1):
    N,M= map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dietotal = []
    
    for i in range(N-M+1): # 0 1 2 3         0
        for j in range(N-M+1): # 0,1,2,3     1
            total = 0 
            for ci in range(i,i+M): # 0 1         0 1
                for cj in range(j,j+M): # 0 1     1 2
                    total += arr[ci][cj]
           
            dietotal.append(total)
            
    print(dietotal)
    
    # [25, 28, 30, 33, 41, 49, 44, 38, 26, 32, 47, 43, 28, 22, 35, 35]
