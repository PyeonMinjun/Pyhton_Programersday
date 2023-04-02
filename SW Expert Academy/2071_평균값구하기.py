n = int(input())

for i in range(n):
    ns = list(map(int,input().split()))
    ns = sum(ns)/10
    print("#{} {}" .format(i+1,round(ns)))