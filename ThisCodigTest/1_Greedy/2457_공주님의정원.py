import sys
input = sys.stdin.readline
n= int(input())

flower = []
for _ in range(n):
    fs,fe,es,ee = list(map(int,input().split()))
    flower.append(( fs * 100 + fe , es * 100 + ee ))

# board.sort()

t = 301
cnt = 0

while t < 1201:
    nxt_t = t 
    
    for f in flower:
        if f[0] <= t and f[1] > nxt_t:
            nxt_t = f[1]
            
    if nxt_t == t:
        print(0)
        exit()
        
        
    cnt += 1
    t = nxt_t

        
print(cnt)