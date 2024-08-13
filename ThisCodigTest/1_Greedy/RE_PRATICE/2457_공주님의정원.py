import sys
input = sys.stdin.readline
n= int(input())

flower = []
for _ in range(n):
    fs,fe,es,ee = list(map(int,input().split()))
    flower.append(( fs * 100 + fe , es * 100 + ee ))


start = 301
cnt= 0
end = 301

while start < 1201:
    for f in flower:
        if f[0] <= start and f[1] > end:
            end = f[1]

    if end == start:
        print(0)
        exit()
    cnt += 1
    start = end
    
print(cnt)