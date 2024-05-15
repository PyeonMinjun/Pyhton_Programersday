n= int(input())
ns = [0]+ [int(input()) for _ in range(n)]
d = [0] * 305 


if n == 1 :
    print(ns[1])
elif n == 2:
    print(ns[1]+ns[2])

else:
    d[1] = ns[1]
    d[2] = ns[2]
    d[3] = ns[3]
    
    for i in range(4,n):
        d[i] =  ns[i] + min(d[i-2],d[i-3])
    
    total = 0
    for i in ns:
        if ns:
            total += i
    print(total - min(d[n-1],d[n-2]))
        