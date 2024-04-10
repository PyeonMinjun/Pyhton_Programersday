n = int(input())

arr = []
for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
    
res = (list(zip(*arr)))


total = []
for i in res:
    total.append(max(i) - min(i))


if n == 1:
    print(0)
else:
    print(total[0] * total[1])
    
