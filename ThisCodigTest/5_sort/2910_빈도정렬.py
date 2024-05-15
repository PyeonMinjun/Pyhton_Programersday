n,c = map(int,input().split())
ns = list(map(int,input().split()))

dict_ns = {}

for i in ns:
    if i in dict_ns:
        dict_ns[i] += 1
    else:
        dict_ns[i] = 1

res = sorted(dict_ns.items(), key = lambda x:-x[1])    

for i ,x in res:
    for j in range(x):
        print(i, end = " ")

            

