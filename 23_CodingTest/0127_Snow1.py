n = int(input())

x1,y1 ,x2,y2 = list(map(int,input().split()))


place = []
rplace= []

for _ in range(n):
    place.append(['*'] * n )

for x in place:
    for k in x:
        rplace.append([k])


for i in range(n):
    print(rplace[i])



