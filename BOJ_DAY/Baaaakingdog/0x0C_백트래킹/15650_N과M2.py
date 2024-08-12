n,m = map(int,input().split())


arr = [0] * 10
# isused = [False] * 10

def func(k):

    if m == k:
        for i in range(m):
            print(arr[i], end = " ")
        print()
        return
    
    start = 1
    if k != 0:
        start = arr[k-1] + 1 

    for i in range(start, n+1):
        arr[k] = i
        func(k+1)

func(0) 
