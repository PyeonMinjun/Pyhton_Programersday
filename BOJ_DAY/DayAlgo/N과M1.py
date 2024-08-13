n,m = map(int,input().split()) # 4 2


arr = [0] * 10
isuesed = [False] * 10


def func(k):

    if k == m:
        for i in range(m):
            print(arr[i], end = " ")
        print()
        return()
    
    for i in range(1,n+1):
        if not isuesed[i]:
            arr[k] = i
            isuesed[i] = True
            func(k+1)
            isuesed[i] = False


func(0)