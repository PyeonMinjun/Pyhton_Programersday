n,m = map(int,input().split()) # 세로,가로
x,y, direction = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
dist = [[0]* n for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
dist[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0 
while True:
    turn_left()
    nx = x + dx[direction]    
    ny = y + dy[direction]
    
    if dist[nx][ny] == 0 and board[nx][ny] == 0:
        dist[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1 
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if board[nx][ny] != 1 and dist[nx][ny] == 1:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(dist)
print(cnt)
        
        
        
        
        
    
        
        
        
    






