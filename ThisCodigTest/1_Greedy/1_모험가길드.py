import time

start_time = time.time()

n = input()
ns = list(map(int,input().split()))
res = 0 
ns = sorted(ns)

for i in ns:
    nss = ns[:i]
    for j in nss:
        if j < len(nss):
            break
    
    del ns[:i]
    res += 1
    
print(res)
end_time = time.time()


print("time = " ,end_time-start_time)