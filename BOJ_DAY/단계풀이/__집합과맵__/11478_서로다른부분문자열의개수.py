

ns = input()
arr = set()    

for j in range(len(ns)):
    for i in range(j,len(ns)):
        arr.add(ns[j:i+1])
print(len(arr))