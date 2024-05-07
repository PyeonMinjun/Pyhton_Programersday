# 다른버전
def d(n):
    nsum = 0
    str_n= str(i)
    result = [str_n]
    
    for i in range(len(str_n)):
        result.append(str_n[i])
    
    for i in result:
        nsum += int(i)
    return nsum

ns = set()
for i in range(1,10001):
    nsum = d(i)
    
    if nsum < 10001:
        ns.add(nsum)

for m in range(1,10001):
    if m not in ns:
        print(m)
    