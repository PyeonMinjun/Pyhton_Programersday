t = int(input())


board = [[0] * 100 for _ in range(100)]

for _ in range(t):
    x,y = map(int,input().split())
    
    for i in range(10):
        for j in range(10):
            board[x+i][y+j] += 1

cnt = 0
for i in board:
    for j in i:
        if j:
            cnt += 1
    
print(board)
print(cnt)
                