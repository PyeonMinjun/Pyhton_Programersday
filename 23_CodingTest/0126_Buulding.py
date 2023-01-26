n = int(input())
bs = list(map(int,input().split()))
maxhigh = 0
Rcnt = 0
Lcnt = 0

for i in range(n):
    if maxhigh < bs[i]:
        maxhigh = bs[i]
        Rcnt += 1


bs = bs[::-1]
maxhigh = 0

for j in range(n):
    if maxhigh < bs[j]:
        maxhigh = bs[j]
        Lcnt += 1

print(Rcnt,Lcnt)