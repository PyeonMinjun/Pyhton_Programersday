n = int(input())
ns = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if ns[i] + ns[j] == 100:
            print(1)
            exit(0)

print(0)
