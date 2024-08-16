n,m  = map(int,input().split())
board = list(map(int,input().split()))
board.sort()

arr = [0]* 10

def dfs(k, start):

    if k == m:
        for i in range(m):
            print(board[arr[i]], end =" ")
        print()
        return
    

    for i in range(start,n):
        arr[k] = i 
        dfs(k+1, i)
        

dfs(0,0)