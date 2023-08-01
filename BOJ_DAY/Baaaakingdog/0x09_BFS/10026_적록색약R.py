from collections import deque
import copy

n = int(input())

board = [list(input()) for _ in range(n)]

board2 = copy.deepcopy(board)

for i in range(n):
    for j in range(n):
        if board2[i][j] == "G":
            board2[i][j] = "R"


dist1 = [[False]* n for _ in range(n)]
dist2 = [[False]* n for _ in range(n)]
dist3 = [[False]* n for _ in range(n)]
dist4 = [[False]* n for _ in range(n)]

q1 = deque()
q2 = deque()
q3 = deque()
q4 = deque()

dx = [0,-1,0,1]
dy = [-1,0,1,0]


def bfsR(x,y):
    dist1[x][y] = True
    q1.append((x,y))
    while q1:
       x,y = q1.popleft()
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == "R" and not dist1[nx][ny]:
                dist1[nx][ny] = True
                q1.append((nx,ny))
        
    return 

def bfsB(x,y):
    dist2[x][y] = True
    q2.append((x,y))
    while q2:
       x,y = q2.popleft()
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == "B" and not dist2[nx][ny]:
                dist2[nx][ny] = True
                q2.append((nx,ny))
        
    return 

def bfsG(x,y):
    dist3[x][y] = True
    q3.append((x,y))
    while q3:
       x,y = q3.popleft()
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == "G" and not dist3[nx][ny]:
                dist3[nx][ny] = True
                q3.append((nx,ny))
        
    return 

def bfsR2(x,y):
    dist4[x][y] = True
    q4.append((x,y))
    while q4:
       x,y = q4.popleft()
       for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board2[nx][ny] == "R" and not dist4[nx][ny]:
                dist4[nx][ny] = True
                q4.append((nx,ny))
        
    return 


cnt = 0
cnt2= 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R' and not dist1[i][j]:
            bfsR(i,j)
            cnt += 1
        if board[i][j] == "B" and not dist2[i][j]:
            bfsB(i,j)
            cnt += 1
            cnt2 += 1
            
        if board[i][j] == "G" and not dist3[i][j]:
            bfsG(i,j)
            cnt += 1
            
        if board2[i][j] == "R" and not dist4[i][j]:
            bfsR2(i,j)
            cnt2 += 1
print(cnt, cnt2)

                

             
        
        


        
            
        

