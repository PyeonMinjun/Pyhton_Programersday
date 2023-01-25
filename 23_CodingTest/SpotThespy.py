n = int(input())

for _ in range(n):
    c = int(input())
    cs = (list(map(int,input().split())))
    arr = cs[:]

    cs.sort()
    del_cs = (cs[1])
    ns = cs.count(del_cs)

    for _ in range(ns):
        cs.remove(del_cs)
    x = cs[0]

    print(arr.index(x)+1)
