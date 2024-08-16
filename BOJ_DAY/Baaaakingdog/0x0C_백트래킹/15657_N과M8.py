n,m = map(int,input().split())

board = list(map(int,input().split()))
board.sort()


arr = [0] * 10
def bfs(k):
    
    if k == m:
        for i in range(m):
            print(board[(arr[i])] , end = " ")
        print()
        return
    
    start = 0
    if k != 0:
        start = arr[k-1] + 1

    for i in range(start, n):
        arr[k] = i
        bfs(k+1)

bfs(0)