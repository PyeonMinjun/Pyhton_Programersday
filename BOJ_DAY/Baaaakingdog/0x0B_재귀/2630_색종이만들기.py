def cheak(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != paper[x][y]:
                return False
    return True

def solve(x,y,z):
    if cheak(x,y,z):
        cnt[paper[x][y]] += 1
        return
    
    n = z//2
    
    for i in range(2):
        for j in range(2):
            solve(x+(i*n), y+(j*n), n)
            
    
N = int(input())
paper = [list(map(int,input().split()))for _ in range(N)]
cnt = [0,0]
solve(0,0,N)

for i in range(2):
    print(cnt[i])