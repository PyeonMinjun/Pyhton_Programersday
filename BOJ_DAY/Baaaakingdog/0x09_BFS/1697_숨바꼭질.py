from collections import deque
n,m = map(int, input().split())

board = [-1 for _ in range(200000)]
q = deque()

board[n] = 0
q.append(n)



while q:
    x = q.popleft()  #x = 5

    for i in [x+1,x-1,x*2]:
        nx = i
        
        if nx < 0 or nx > 100000 or board[nx] != -1:
            continue
        
        
        
        # if board[m] >= 0:
        #     print(board[m])
        #     exit(0)
        
        board[nx] = board[x] + 1
        q.append(nx)
    
print(board[m])