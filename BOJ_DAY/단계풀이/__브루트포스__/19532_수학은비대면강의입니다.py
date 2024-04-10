a,b,c,q,w,e = map(int,input().split())

for i in range(-999,1000):
    for j in range(-999,1000):
        if (a*i) + (b*j) == c and (q*i) + (w*j) == e:
            print(i,j)