n = int(input())
ns = list(map(int, input().split()))

for i in ns:
    max1 = 0
    min1 = 0
    for k in range(n):
        if i > ns[k]:
            min1 += 1
    max1 = (n - min1) - 1
    print(min1, max1) 