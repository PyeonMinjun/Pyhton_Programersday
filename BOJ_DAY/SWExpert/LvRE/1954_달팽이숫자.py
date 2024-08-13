t= int(input())

for tc in range(1,t+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    x,y,dr = 0,0,0
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    cnt = 1
    board[x][y] = 1
    cnt += 1

    while cnt <=  n * n:
        nx = x + dx[dr]
        ny = y + dy[dr]

        if 0 <= nx < n and  0 <= ny < n and board[nx][ny] == 0 :
            board[nx][ny] = cnt
            x,y = nx,ny
            cnt += 1
            
        else:
            dr = (dr+1) % 4

    print("#{}"  .format(tc))
    for i in board:
        print(*i)
