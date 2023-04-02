n = int(input())

for i in range(n):
    x = int(input())
    ns = list(map(int,input().split()))
    ns = ns[::-1]
    sum = 0
    result = ns[0]
    for j in ns[1:]:
        if result > j:
            sum += result - j
        else:
            result = j
    print("#{} {}" .format(i+1,sum))