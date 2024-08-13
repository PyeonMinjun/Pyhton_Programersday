n= int(input())
ns = list(map(int,input().split()))

ns.sort()

s= ns[0]
res = [ns[0]]
for i in range(1,n):
    s += ns[i]
    res.append(s)
    
    
print(sum(res))