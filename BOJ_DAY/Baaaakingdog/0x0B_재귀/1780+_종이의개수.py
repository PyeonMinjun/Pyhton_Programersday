def cheak(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[x][y] != board[i][j]:
                return False
    return True

def solve(x,y,z):
    if cheak(x,y,z):
        cnt[board[x][y]+1] += 1
        return

    n = z // 3
    
    for i in range(3):
        for j in range(3):
            solve(x + (i*n), y+ (j*n) ,n)
            
    
        
        

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]
cnt = [0,0,0]
solve(0,0,N)

print(cnt)