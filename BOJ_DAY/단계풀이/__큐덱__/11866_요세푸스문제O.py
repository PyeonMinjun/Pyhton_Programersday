n,m = map(int, input().split()) 

dat = [i + 1 for i in range(n)]
res = []
cnt = 0 

for _ in range(n):
    cnt += m-1 # 2 4
    if cnt >= len(dat):
        cnt = cnt % len(dat)
    res.append(dat.pop(cnt))

