from collections import deque
import copy
n = int(input())

board = [list(input()) for _ in range(n)]
vis = [[False]* n for _ in range(n)]
vis2 = [[False]* n for _ in range(n)]
board2 = copy.deepcopy(board)

for i in range(n):
    for j in range(n):
        if board2[i][j] == "G":
            board2[i][j] = "R"


q1= deque() # R
q2= deque() # G
q3= deque() # B
q4 = deque()



dx = [0,-1,0,1]
dy = [-1,0,1,0]
cnt = 0
j_cnt = 0

for o in range(n):
    for p in range(n):
        if board[o][p] == "R" and not vis[o][p]:
            q1.append((o,p))
            cnt += 1

            while q1:
                x,y = q1.popleft()
                vis[x][y] = True
                
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny <0 or ny >= n:
                        continue
                    
                    if board[nx][ny] == "R" and not vis[nx][ny]:
                        q1.append((nx,ny))
                        vis[nx][ny] = True
                        
                        
for o in range(n):
    for p in range(n):
        if board[o][p] == "B" and not vis[o][p]:
            q2.append((o,p))
            cnt += 1
            j_cnt += 1
            

            while q2:
                x,y = q2.popleft()
                vis[x][y] = True
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny <0 or ny >= n:
                        continue
                    
                    if board[nx][ny] =="B" and not vis[nx][ny]:
                        q2.append((nx,ny))
                        vis[nx][ny] = True
                        

for o in range(n):
    for p in range(n):
        if board2[o][p] == "R" and not vis[o][p]:
            q3.append((o,p))
            cnt += 1
            

            while q3:
                x,y = q3.popleft()
                vis[x][y] = True
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny <0 or ny >= n:
                        continue
                    
                    if board[nx][ny] =="G" and not vis[nx][ny]:
                        q3.append((nx,ny))
                        vis[nx][ny] = True



for o in range(n):
    for p in range(n):
        if board2[o][p] == "R" and not vis2[o][p]:
            q4.append((o,p))
            j_cnt += 1

            while q4:
                x,y = q4.popleft()
                vis2[x][y] = True
                
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= n or ny <0 or ny >= n:
                        continue
                    
                    if board2[nx][ny] == "R" and not vis2[nx][ny]:
                        q4.append((nx,ny))
                        vis2[nx][ny] = True
                        
print(cnt, j_cnt)