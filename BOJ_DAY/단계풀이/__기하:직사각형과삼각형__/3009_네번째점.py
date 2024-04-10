a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

resx = -1 
resy = -1


if a != c:
    if a != e:
        resx = a
    else:
        resx = c
else:
    resx = e

if b != d:
    if b != f:
        resy = b
    else:
        resy = d
else:
    resy = f

print(resx,resy)
    

