import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ns = [0] + list(map(int,input().split()))
d = [0] * (n+1)
t= 0

for i in range(1,n+1):
    t += ns[i]
    d[i] = t
    
    
for i in range(m):
    x,y = map(int,input().split())
    print(d[y]- d[x-1])