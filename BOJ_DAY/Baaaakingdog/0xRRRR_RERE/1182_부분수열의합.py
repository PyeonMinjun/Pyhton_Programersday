n,m = map(int,input().split())
board = list(map(int,input().split())) + [0]

cnt = 0
def dfs(depth,tot):
    global cnt 
    # 기저 
    if depth == n:
        if tot == m:
            cnt += 1        
        return

    dfs(depth+1, board[depth] + tot) # 선택 O
    dfs(depth+1, tot) # 선택 X


dfs(0,0)
print(cnt)