from collections import deque
n,m,v = (map(int,input().split()))


board = [[False] * m for _ in range(n+1)]

#방문배열
vis1= [False] * (n+1)
vis2= [False] * (n+1)


for i in range(m):
    x, y = (map(int,input().split()))
    board[x][y] = True
    board[y][x] = True

def dfs(v):
    print(v,end=" ")
    for i in range(1,n+1):
        if not vis2[i]  and board[v][i]== True:
            vis2[v] = True
            dfs(i)
            





# def bfs(v):
#     q = deque([v])
#     vis1[v] = True
#     while q:
#         v = q.popleft()
#         print(v, end = " ")
#         for i in range(1,n+1):
#             if not vis1[i]  and board[v][i]== True:
#                 q.append(i)
#                 vis1[i] = True
vis2[v] = True
dfs(v)
print()


q = deque([v])

while q:
    v = q.popleft()
    vis1[v]= True
    print(v, end = " ")
    for i in range(1,n+1):
        if not vis1[i] and board[v][i]:
            q.append(i)
            vis1[i]= True
        
