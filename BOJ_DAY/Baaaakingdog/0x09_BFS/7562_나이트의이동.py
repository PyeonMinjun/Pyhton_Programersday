from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    b_cnt = int(input())
    
    n,m = list(map(int,input().split()))
    ns,ms = list(map(int,input().split()))
    
    board = [[-1] * b_cnt for _ in range((b_cnt))] 
    
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [-1,-2,-2,-1,1,2,2,1]
    
    q = deque()
    board[n][m] = 0
    q.append((n,m))
    
    
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= b_cnt or ny < 0 or ny >= b_cnt:
                continue
            if board[nx][ny] >= 0:
                continue
            board[nx][ny] = board[x][y] + 1
            q.append((nx,ny))
    
    print(board[ns][ms])
            
    