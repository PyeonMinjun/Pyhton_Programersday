t = int(input())

for tc in range(1,t+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x = 0
    y = 0
    cnt = 1
    r = 0
    board[x][y]= cnt
    cnt += 1
    
    while cnt <= N*N:
        nx = x + dx[r]
        ny = y + dy[r]
        
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            x = nx
            y = ny
            board[nx][ny] = cnt
            cnt += 1
        
        else:
            r = (r+1) % 4
    
    print("#{}" . format(tc))
    for i in board:
        print(*i)
        