t = int(input())

dx = [0,1,0,-1] 
dy = [1,0,-1,0]

for tc in range(1,t+1):
    N = int(input())
    
    arr= [[0] * N for _ in range(N)]
    
    x,y,dr = 0,0,0
    arr[x][y] = 1
    cnt = 2
    
    while cnt <= N * N:
        nx,ny = x+dx[dr], y+dy[dr]
        
        if 0<= nx < N and 0<= ny < N and arr[nx][ny] == 0:
            x, y = nx, ny
            arr[x][y] = cnt
            cnt += 1
        else:
            dr  = (dr +1) % 4
            
    for ls in arr:
        print(*ls)    
     