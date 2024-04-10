n = int(input())
ns = list(map(int,input().split()))

xs = [0] * 100


for i in ns:
    xs[i] += 1
    if xs[100-i]:
        print(1)
        exit(0)
    
print(0)
    