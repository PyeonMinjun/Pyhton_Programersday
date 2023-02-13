n = int(input())
ns = input()
nss = list(str(ns))
res = [0] * 27

# 97 ~ 123
# 1 26
cnt = 0
mid = False

for i in nss:
    o = ord(i) - 96
    res[o] += 1
    if res[o] >= 2:
        mid = o
        break
    else:
        cnt += 1
        
if mid == False:
    print(cnt)
    exit(0)
    
mid = chr(mid+96)
scr= ns.index(mid,ns.index(mid)+1)
left = ns[:scr]
right = ns[scr:]


arr2 = [0] * 27
for i in right:
    o2 = ord(i)-97
    arr2[o2] = 1


maxPlace= (len(left) + arr2.count(1))
print(maxPlace)