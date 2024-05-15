res = []

try:
    while True:
        for i in (input().split()):
            res.append("".join(i))
            

except(EOFError):
    pass

tot = []
for i in res[1:]:
    k = ''
    for j in i[::-1]:
        k += j
    tot.append(int(k))

tot.sort()

for i in tot:
    print(i)