from collections import deque
import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
    excape = True
    m,n = list(map(int,input().split()))
    
    board = [list(input()) for _ in range(n)]
    
    dist = [[-1]*m for _ in range(n)]
    dist2 = [[-1]*m for _ in range(n)] # 불
    
    q= deque()
    q2 = deque()
    
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    
    for i in range(n):
        for j in range(m):
            if board[i][j]  == "@":
                # board[i][j] = 0
                q.append((i,j))
                dist[i][j] = 0
            
            elif board[i][j] == "*":
                dist2[i][j] = 0
                q2.append((i,j))
    
    # 불
    while q2:
        x,y = q2.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                            
            if board[nx][ny] == "#" or dist2[nx][ny] >= 0:
                continue
            
            dist2[nx][ny] = dist2[x][y] + 1
            q2.append((nx,ny))
 
    
    while q and excape:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print(dist[x][y]+1)
                excape = False
                break  
                             
            if board[nx][ny] == "#" or dist[nx][ny] >= 0:
                continue
        
            if  dist[nx][ny] == -1 or dist2[nx][ny] > dist[x][y]+1: # -1 > 1
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    
    if excape:
        print("IMPOSSIBLE")
       
    