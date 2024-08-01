from collections import deque
import sys
input = sys.stdin.readline



n,m = (map(int,input().rsplit().split()))
board = [list(map(int,input())) for _ in range(n)]
dis = [[False]* m for _ in range(n)]


q = deque()
q.append((0,0))
dis[0][0] = True
dx = [0,-1,0,1]
dy = [-1,0,1,0]


while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dis[nx][ny] == False and board[nx][ny] == 1:
            dis[nx][ny] = True
            board[nx][ny] = board[x][y] + 1
            q.append((nx,ny))

print(board[n-1][m-1])