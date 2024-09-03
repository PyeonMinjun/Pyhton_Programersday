board = [list(map(int,input())) for _ in range(4)]
n = int(input())

def rotate_wheel(x, dir):
    dirs = [0] * 4
    dirs[x] = dir
    idx =x 
    # 왼쪽 전파 
    while idx > 0 and board[idx-1][2] != board[idx][6]:
        dirs[idx-1] = -dirs[idx]
        idx -= 1
    
    # 오른쪽 전파 
    idx = x
    while idx < 3 and board[idx][2] != board[idx+1][6]:
        dirs[idx+1] = -dirs[idx]
        idx += 1

    for i in range(4):
        if dirs[i] == -1:
            board[i] = board[i][1:] + [board[i][0]]
        elif dirs[i] == 1:
            board[i] = [board[i][-1]]  + board[i][:-1]



for _ in range(n):
    x,dir = map(int,input().split())
    rotate_wheel(x-1, dir)

res = 0

if board[0][0] == 1:
    res += 1

if board[1][0] == 1:
    res += 2

if board[2][0] == 1:
    res += 4

if board[3][0] == 1:
    res += 8




print(res)








