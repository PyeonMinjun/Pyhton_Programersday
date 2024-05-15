import sys
input = sys.stdin.readline

n,m = (map(int,input().split()))
ns = [0]+ list(map(int,input().split()))


d = [0] * (n+1)
d[1] = ns[1]


for i in range(len(ns[1:])+1):
    d[i] = d[i-1] + ns[i]

for _ in range(m):
    i,j = map(int,input().split())
    print(d[j]- d[i-1])