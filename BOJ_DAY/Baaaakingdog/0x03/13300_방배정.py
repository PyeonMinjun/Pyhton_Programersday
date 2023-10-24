n, k  = map(int,input().split())

arr= [[0,0] for _ in range(7)]
cnt= 0

for _ in range(n):
    s,y = map(int,input().split())
    # if arr[y][s] >= k:
    #     cnt += 1
    arr[y][s] += 1
    

for i in range(7):
    for j in range(2):
        cnt += arr[i][j] // k
        
        if arr[i][j] % k:
            cnt += 1

print(cnt)
        