n= int(input())
ns = []

for i in range(n):
    ns.append(list(map(int,input().split())))

cnt = 0
for i in ns:
    sum = 0
    for j in i:
        if j % 2:
            sum += j
    cnt += 1
            
    print("#{} {}" .format(cnt,sum))

        
