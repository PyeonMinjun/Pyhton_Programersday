n,m = map(int,input().split())
board = list(map(int,input().split()))
board.sort()

arr = [0] * 10
isused = [False] * 10

res = []
def dfs(k):

    if k == m:
        # tmp = []
        for i in range(m):
            # tmp.append(board[arr[i]])
            print(arr[i], end=" ")
        print()

        # if tmp not in res:
        #     res.append(tmp)
        return

    tmp = 0
    for i in range(n):
        if not isused[i] and tmp != board[i]: 
            arr[k] = board[i]
            isused[i] = True
            tmp = arr[k]
            dfs(k+1)
            isused[i] = False

dfs(0)

# res = list(map(list,set(map(tuple, res))))
# res.sort()

# for i in res:
#     print(*i)

