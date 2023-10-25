n, k = list(map(int,input().split()))
pre = [0] * 5001
nxt = [0] * 5001




# pre = [n if i == 1 else i-1 for i in range(1,n+1)]
# nxt = [1 if i == n else i+1 for i in range(1,n+1)]

for i in range(1,n+1):
    pre[i] = n if i==1 else i-1
    nxt[i] = 1 if i==n else i+1



res = []
cur = 1
i = 1

while n != 0:
    if i == k:
        pre[nxt[cur]] = pre[cur]
        nxt[pre[cur]] = nxt[cur]
        res.append(cur)
        i = 1
        n -= 1
    else:
        i+=1 
    cur = nxt[cur]
            

print("<"+", ".join(map(str,res))+">")
    
print("<{}>" .format(", ".join(map(str,res))))