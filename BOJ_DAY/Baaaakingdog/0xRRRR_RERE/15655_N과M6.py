n,m = map(int,input().split())
board = list(map(int,input().split())) + [0]


arr = [0] * 10
isused = [False] * 10
board.sort()

def func(k):
    if m == k:
        for i in range(m):
            print(board[arr[i]], end = " ")
        print()
        return
    
    st = 1
    if k!= 0:
        st = arr[k-1] + 1

    
    for i in range(st,n+1):
        if not isused[i]:
            arr[k] = i 
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)

