n= int(input())
ns = [input() for _ in range(n)]
ns = set(ns)
ns= list(ns)
ns.sort(key = lambda x:(len(x),x))

for i in ns:
    print(i)

