import math
n = int(input())
for tc in range(1,n+1):
    ns = list(map(int,input().split()))
    
    print("#{} {}" .format(tc, round(sum(ns) / 10)))