from collections import deque
t = int(input())



# def bfs(x,y):
    
    


for _ in range(t):
    n, m ,k = list(map(int,input().split()))
    
    board = [[-1]* m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    
    
    for _ in range(k):
        a,b = list(map(int,input().split()))
        board[a][b] = 1
        
    cnt = 0
    q = deque()     
   
        

    for o in range(n):
        for p in range(m):
            if board[o][p] == 1 and not vis[o][p]:
                cnt += 1
                    
                q.append((o,p))
                vis[o][p] = True
            
                        
                while q:
                    x,y = q.popleft()
                    
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        
                        if board[nx][ny] == 1 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                
                
    print(cnt)
    
        
        