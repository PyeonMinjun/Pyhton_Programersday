n = int(input())

firs = list(map(int,input().split()))
secs = list(map(int,input().split()))

firs.sort(reverse=True)
secs.sort()


res = 0
for i in range(n):
    res += firs[i] * secs[i] 

print(res)