n = int(input())
ns = [int(input()) for _ in range(n)]

ns.sort()

cnt = 1
mxcnt = 0
mxval = ns[0]

for i in range(n-1):
    if ns[i] == ns[i+1]:
        cnt += 1
    else:
        if cnt > mxcnt:
            mxcnt = cnt
            mxval = ns[i]
        cnt = 1
    if i == n-2 and cnt > mxcnt:
        mxval = ns[i]
        
        
print(mxval)
        