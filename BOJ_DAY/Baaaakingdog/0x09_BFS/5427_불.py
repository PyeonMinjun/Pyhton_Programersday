from collections import deque
t = int(input())


for _ in range(t):
    escape = True
    
    w,h = map(int,input().split())
    board = [list(input()) for _ in range(h)]
    arr1 = [[-1] * w for i in range(h)]
    arr2 = [[-1] * w for i in range(h)]
    
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    
    q1 = deque()
    q2 = deque()
    
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                arr1[i][j] = 0
                q1.append((i,j))
                
            if board[i][j] == "@":
                arr2[i][j] = 0
                q2.append((i,j))
                
    while q1:
        x,y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or  nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] == "#" or arr1[nx][ny] >= 0:
                continue
            
            arr1[nx][ny] = arr1[x][y] + 1
            q1.append((nx,ny))
            
    while q2 and escape:
        x,y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or  nx >= h or ny < 0 or ny >= w:
                print(arr2[x][y]+1)
                escape = False
                break
                        
            if board[nx][ny] == "#" or arr2[nx][ny] >= 0:
                continue
                
            if arr1[nx][ny] != -1 and arr1[nx][ny] <= arr2[x][y]+1:
                continue
                            
            arr2[nx][ny] = arr2[x][y] + 1
            q2.append((nx,ny))
            
    if escape:
        print("IMPOSSIBLE")
            
            