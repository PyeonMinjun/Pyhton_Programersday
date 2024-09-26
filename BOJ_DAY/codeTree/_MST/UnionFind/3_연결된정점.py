n, m = (map(int, input().split()))

uf = [0] * (n + 1)
sz = [0] * (n + 1)

for i in range(1, n + 1):
    uf[i] = i
    sz[i] = 1


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)

    if X != Y:
        uf[Y] = X
        sz[X] += sz[Y]


for _ in range(m):
    command = input()
    query = command[0]

    if query == 'x':
        a, b = (map(int, command[2:].split()))
        union(a, b)
    else:
        a = int(command[2:])
        a = find(a)
        print(sz[a])