n,m = map(int,input().split())
board = list(map(int,input().split()))
board.sort()

# 조합
arr= [0]* 10
isused = [False] * 10


def dfs(k,start):
    
    if k == m:
        for i in range(m):
            print(arr[i], end = " ")
        print()
        return
    
    tmp = 0
    for i in range(start, n):
        if tmp != board[i]: # 예외처리  이전 조합의 마지마 항과 그다음 항의 마지막 항이 같으면 pass
            arr[k] = board[i]
            tmp = arr[k]
            dfs(k+1,i+1)

dfs(0,0)