n = int(input())

flower = []

for _ in range(n):
    fs,fe,es,ee = list(map(int,input().split()))
    flower.append((fs * 100 + fe ,es * 100 + ee))

t = 301
cnt = 0

while t < 1201:
    end_t = t
    for f in flower:
        if f[0] <= t and end_t < f[1]:
            end_t = f[1]
        
    if t == end_t:
        print(0)
        exit()
    cnt +=1
    t = end_t
    
    
print(cnt)
        
    


    