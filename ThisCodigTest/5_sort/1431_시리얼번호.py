def sum_ns(s):
    res = 0
    for v in s:
        if v.isdigit():
            res += int(v)
    return res
n = int(input())
ns = [input() for _ in range(n)]

ns.sort(key =  lambda x : (len(x), sum_ns(x),x))
for i in ns:
    print(i)
