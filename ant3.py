t  = int(input())

for _ in range(t):
    len , wall = map(int,input().split()) 
    s = input()                           
    cnt = 0
    cnz = 0
    x = s.find("@")
    zx = x
    y = s.find("O")
    z = s.find("G")

    if zx < z:
        res_z = s[zx:z]
    elif zx > z:
        zx, z = z ,zx 
        res_z = s[zx:z]
    
    if x < y:
        result = s[x:y]
    elif x > y:
        x ,y = y,x
        result = s[x:y]

    for fz in res_z:
        if fz =="#":
            cnz +=1

    for f in result:
        if f == "#":
            cnt += 1

    if (cnt <= wall) or (cnz <= wall):
        print("HAHA!")
    else:
        print("HELP!")

