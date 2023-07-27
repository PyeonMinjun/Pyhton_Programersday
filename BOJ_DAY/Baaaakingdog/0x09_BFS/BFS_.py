from collections import deque
N,M = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs(x,y):
    area = 1
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                area += 1
    return area

cnt = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i,j))
            
            
print(cnt)
print(max_area)    