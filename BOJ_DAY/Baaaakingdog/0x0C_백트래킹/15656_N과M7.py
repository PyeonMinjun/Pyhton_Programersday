n ,m = map(int,input().split())

board = list(map(int,input().split()))
board.sort()
arr = [0] * 10
isused = [False] * 10


def func(k):
    if m == k:
        for i in range(m):
            print(board[arr[i]], end = " ")
        print()
        return
    
    for i in range(n):
        arr[k] = i
        isused[i]= True
        func(k+1)
        isused[i]= False



func(0)


