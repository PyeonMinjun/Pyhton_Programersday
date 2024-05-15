n = int(input())
ns = [0] + [int(input()) for _ in range(n)]
d = [0] *  (n+1)



if n == 1:
    print(ns[1])
elif n == 2:
    print(ns[1]+ ns[2])

else:
    d[1] = ns[1]
    d[2] = ns[2]
    d[3] = ns[3]
    for i in range(4,n+1):
        d[i] = min(d[i-2],d[i-3]) + ns[i]
        
    
    print(sum(ns) - min(d[n-1], d[n-2]))
