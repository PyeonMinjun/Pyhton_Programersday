from collections import deque
n, m = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(m)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]


q = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i,j))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny <n and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] +1
            q.append((nx,ny))

# print(board)
max_board = 0
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    max_board = max(max_board,max(i))
                
print(max_board-1)



