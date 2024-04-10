n = int(input())

top = list(map(int,input().split()))

res = [0]

for i in range(1,n):
    cnt = 1

    if top[i] < top[i-cnt]:
        res.append(i-cnt+1)
                
    else:
        while True:
            cnt += 1
            if i-cnt < 0:
                res.append(0)
                break
            elif top[i] < top[i-cnt]:
                res.append(i-cnt+1)
                break
print(res)
    