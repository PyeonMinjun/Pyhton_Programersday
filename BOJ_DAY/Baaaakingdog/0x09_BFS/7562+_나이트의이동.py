from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = int(input())
    n,m = map(int,input().split())
    rn,rm = map(int,input().split())
    
    board = [[0]* l for _ in range(l)]
    #dist = [[-1]* l for _ in range(l)]
    
    board[n][m] = 1
    #dist[n][m] = 0
    
    q = deque()
    q.append((n,m))
    
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    
    while q:
        x,y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            
            if board[nx][ny] == 0: #and dist[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))
                #dist[nx][ny] = 0
                
    print(board[rn][rm]-1)