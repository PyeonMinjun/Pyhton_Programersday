# 241011

n = int(input())
dragons = [list(map(int,input().split())) for _ in range(n)]
board = [ [0]* 104 for _ in range(104) ]


cnt = 0

for dg in dragons:
    r,c,d,g = dg
    v = [d % 4]
    board[c][r] = 1
    for _ in range(g):
        vsize = len(v)
        for j in range(vsize-1, -1, - 1):
            v.append((v[j]+1) % 4)
    for dir in v:
        if dir == 0:
            r += 1
        elif dir == 1:
            c -= 1
        
        elif dir == 2:
            r -= 1

        elif dir == 3:
            c += 1

        board[c][r]= 1  


for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1

# for i in board:
    # print(i)
print(cnt)