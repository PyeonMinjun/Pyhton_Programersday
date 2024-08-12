from collections import deque
n, m, v = map(int,input().split())

init = (list(map(int,input().split())) for _ in range(m))

board = [[False] * (n+1) for _ in range(n+1)]
vis1 = [False] * (n+1)
vis2 = [False] * (n+1)


for x,y in init:
    board[x][y] = 1
    board[y][x] = 1

# def dfs_stack(v):
#     s = [v]
#     while s:
#         node = s.pop()
#         if not vis2[node]:
#             vis2[node] = True
#             print(node, end=" ")
#             for i in range(n, 0, -1):
#                 if board[node][i] and not vis2[i]:
#                     s.append(i)

def dfs(v):
    vis2[v] = True
    print(v, end = ' ')
    for i in range(1,n+1):
        if not vis2[i] and board[v][i] == 1:
            dfs(i)



def bfs(v):
    q = deque([v])
    vis1[v] = True
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1,n+1):
            if not vis1[i] and board[v][i] == 1:
                q.append(i)
                vis1[i] = True



# dfs_stack(v)
print()
dfs(v)
print()
bfs(v)



    

