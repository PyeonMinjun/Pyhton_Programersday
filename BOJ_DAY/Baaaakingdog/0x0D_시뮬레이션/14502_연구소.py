from itertools import combinations
from collections import deque

    
# 입력값
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

clean = []
virus = []
existing_walls = []
q = deque()
dx = [0,-1,0,1]
dy = [-1,0,1,0]
vis = [[False]* m for _ in range(n)]

# 0의 위치 값  
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            clean.append((i,j))

        elif board[i][j] == 2:
            virus.append((i,j))

        elif board[i][j] == 1:
            existing_walls.append((i,j))
            vis[i][j] = True

res = 0
for walls in combinations(clean,3):
    board2 = [raw[:] for raw in board]
    vis2 = [raw[:] for raw in vis]

    for wx,wy in walls:
        board2[wx][wy] = 1
        vis2[wx][wy] = True
    
    q = deque(virus)

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board2[nx][ny] == 1 or vis2[nx][ny] == True:
                continue
            
            board2[nx][ny] = 2
            vis2[nx][ny] = True
            q.append((nx,ny))

    novirus = 0
    # for i in range(n):
    #     for j in range(n):
    #         if vis2[i][j] == False:
    #             novirus += 1
    novirus = sum(1 for i in range(n) for j in range(m) if board2[i][j] == 0)


    res = max(novirus, res)
print(res)