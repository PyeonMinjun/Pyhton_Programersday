n,s = map(int,input().split())
board = list(map(int,input().split()))# 5

arr = [0] * 100


def func(k, start):
    if k == cnt:
        for i in range(cnt):
            print(arr[i], end = " ")
        print()
        return
    

        for i in range(start,n):
            arr[k] = board[i]
            func(k+1)

func(0)

