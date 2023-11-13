t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(1,t+1):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    
    x= 0
    y= 0
    cnt = 1
    dr = 0
    board[x][y] = cnt
    cnt+= 1
    
    while cnt <= n*n:
        nx = x + dx[dr]
        ny = y + dy[dr]
           
        # if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nx = x - dx[dr]
            ny = y - dy[dr]
           
        if board[nx][ny] == 0:
            x,y = nx,ny
            board[nx][ny] = cnt
            cnt += 1   
            
        else:
            dr = (dr+1)% 4
            
    print("#{}" .format(tc))
    
    for i in board:
        print(" ".join(map(str,i)))
        
            
    
            
        
        
        
        
        
    