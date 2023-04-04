T = int(input())

for tk in range(T):
    N = int(input())
    
    arr = [[0]* N for _ in range(N)] 
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y,dr = 0,0,0
    cnt = 1
    arr[x][y] = cnt
    cnt += 1
    
    while cnt <= N * N :
        nx,ny= x+dx[dr], y+dy[dr]
        
        if 0 <= nx < N and 0 <= ny < N and  arr[nx][ny] == 0:
            x,y = nx,ny
            arr[x][y] = cnt
            cnt += 1
        else:
            dr = ( dr+1 ) % 4
    
    print('#{}' .format(tk+1))
    for ls in arr:
        print(*ls)
            
    
    