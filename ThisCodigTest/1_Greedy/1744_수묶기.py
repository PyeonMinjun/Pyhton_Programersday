n = int(input())

ns = [int(input()) for _ in range(n)]


minus = []
plus = []

for i in ns:
    if i <= 0:
        minus.append(i)
    else:
        plus.append(i)
        
plus.sort(reverse=True)
minus.sort()
k = 0 
res = 0

if len(plus) % 2 != 0:
    res += plus[-1] 

for z1,z2 in zip(plus[k::2],plus[k+1::2]):
    if z1 == 1 or z2 == 1:
        res += z1 + z2
    else:
        res += z1 * z2

if len(minus) % 2 != 0:
    res += minus[-1]    

for z1,z2 in zip(minus[k::2],minus[k+1::2]):
    res += z1 * z2

print(res)
