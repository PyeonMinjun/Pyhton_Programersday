n,m = map(int,input().split())


arr = [0] * 10
isused = [False] * 10

def fucn(k):
    if k == m:
        for i in range(m):
            print(arr[i], end =" ")
        print()
        return
    
    start = 1
    if k != 0:
        start = arr[k-1]

    for i in range(start, n+1):
        arr[k] = i
        fucn(k+1)       

fucn(0)
