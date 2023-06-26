n = int(input())

for tc in range(1,n+1):
    ns = list(map(int,input().split()))
    ns.sort()
    total = round(sum(ns[1:9]) / 8)
    
    print("#{} {}" .format(tc, total))