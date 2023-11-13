t = int(input())
for tc in range(1,t+1):
    n = int(input())
    board = [[0]* (n+1) for _ in range(n+1)]
    board[1][1] = 1
        
    for i in range(2,n+1):
        for j in range(1,i+1):
            board[i][j] = board[i-1][j] + board[i-1][j-1]
    arr = (board[1:])
    print("#{}" . format(tc))
    for i in arr:
        for j in i:
            if j == 0:
                continue
            else:
                print(j, end = " ")
        print()
                
    