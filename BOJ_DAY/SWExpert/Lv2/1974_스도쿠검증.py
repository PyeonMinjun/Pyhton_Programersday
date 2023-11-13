t = int(input())

for tc in range(1,t+1):
    flag = True
    board = [list(map(int,input().split())) for _ in range(9)]
    
    for i in board:
        if len(set(i)) != 9:
            flag = False
    
    board = list(zip(*board))
    
    for i in board:
        if len(set(i)) != 9:
            flag = False

    
    for i in range(0,9,3):
        for j in range(0,9,3):
            if len(set(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])) != 9:
                flag = False


    if flag:
        print(1)
    else:
        print(0)