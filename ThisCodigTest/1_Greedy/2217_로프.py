n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort()


res = []

for k in range(1,n+1):
    res.append(rope[n-k] * k)

print(max(res))