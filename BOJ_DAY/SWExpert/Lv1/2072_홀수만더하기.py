t=int(input())
for tc in range(1,t+1):
    ns= list(map(int,input().split()))
    res = 0
    for i in ns:
        if i % 2 != 0:
            res += i
    print("#{} {}" .format(tc,res))