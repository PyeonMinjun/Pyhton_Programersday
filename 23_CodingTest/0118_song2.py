n = int(input())
songlist = [input() for _ in range(n)]
songsec = [int(input()) for _ in range(n)]

n_asksg = int(input())
asksong = [int(input()) for _ in range(n_asksg)]


total_sg  = [0]
sumTime = sum(songsec)

addsong = 0 
for x in songsec:
    addsong += x
    total_sg.append(addsong)

for i in range(n_asksg):
    cnt = 0
    if asksong[i] > sumTime :
        for j in range(i,len(asksong)):
            asksong[j] -= sumTime
        
    for c1, c2 in zip(total_sg,total_sg[1:]):
        if c1 + 1 <= asksong[i] <= c2:
            print(songlist[cnt])
            break
   

        else:
            cnt += 1