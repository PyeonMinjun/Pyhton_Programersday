t = int(input())

for tc in range(1,t+1):
    n,k = list(map(int,input().split()))
    board = [list(map(int,input().split())) + [0] for _ in range(n)] +[[0] * (n+1)]   
    
    ret = 0
    
    for lst in board:
        cnt = 0
        
        for j in range(len(lst)):
            if lst[j]:
                cnt += 1
            else:
                if cnt == k:
                    ret += 1
                cnt = 0
                
    c_board = list(zip(*board))
    
    for lst in c_board:
        cnt = 0
        
        for j in range(len(lst)):
            if lst[j]:
                cnt += 1
            else:
                if cnt == k:
                    ret += 1
                cnt = 0
                
                
                
    print(ret)
        