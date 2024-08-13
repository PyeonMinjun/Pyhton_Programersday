n= int(input())

ns = [int(input()) for _ in range(n)] 

wsum = []
hsum = []

for i in ns:
    if i <= 0:
        hsum.append(i)
        
    else:
        wsum.append(i) 

wsum.sort(reverse=True)
hsum.sort()

res= 0
if len(wsum) % 2 != 0:
    res += wsum[-1]
for i,j in zip(wsum[::2], wsum[1::2]):
    if i == 1 or j == 1:
        res += i+j
    else:
        res += i * j
    


if len(hsum) % 2 != 0:
    res += hsum[-1]
    
    
for i,j in zip(hsum[::2], hsum[1::2]):
    res += i * j

    
print(res)