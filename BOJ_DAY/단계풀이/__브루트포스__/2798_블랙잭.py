n,m = map(int,input().split())
ns = list(map(int,input().split()))

arr = []

for i in range(n-2):  
    for j in range(i+1,n-1): 
        for k in range(j+1,n):
            
            if ns[i] + ns[j] + ns[k] <= m:
                arr.append(ns[i] + ns[j] + ns[k])

print(max(arr))
