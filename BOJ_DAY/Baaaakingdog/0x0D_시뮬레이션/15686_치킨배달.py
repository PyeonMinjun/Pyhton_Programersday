n,m = map(int,input().split())
board = [map(int,input().split()) for _ in range(n)]


isused = [False] * n
# chiken = []
chiken = [(0,0),(0,1),(0,2)] ## 
arr = [0] * 1000000
tmp = []
dosi = []

def dfs(k):
    if k == m:
        for i in range(m):
            tmp.append(chiken[i])
        return
    
    start = 1
    if k != 0:
        start = arr[k-1] 

    for i in range(start, ):
        chiken[k] = i
        dfs(k+1)

print(tmp)


# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1:
#             chiken.append((i,j))
        
#         if board[i][j] == 2:
#             dosi.append((i,j))


# for i in range(len(chiken)): # 치킨의 수만큼..
    




        
