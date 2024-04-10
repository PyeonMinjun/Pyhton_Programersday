t = int(input())

for tc in range(1,t+1):
    n,m =  map(int,input().split())
   
    board = [list(map(int,input().split())) for _ in range(n)]
    
    dietotal = []
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            
            for si in range(i,i+m):
                for sj in range(j,j+m):
                    total += board[si][sj]
            dietotal.append(total)
            
    print("#{} {}" .format(tc, max(dietotal)))