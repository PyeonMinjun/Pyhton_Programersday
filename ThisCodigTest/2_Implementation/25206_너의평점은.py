from math import *

sumg = 0
suma = 0
for t in range(20):
    ns =  list(input().split())


    alplist = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
    target = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]


   
    for n in ns:
        g = float(ns[1])
        a = ns[2]
        if a == "P":
            continue
        
        sumg += g
        for i in alplist:
            if i == a:
                k = alplist.index(i)
                suma += (g * target[k])
                break
print(round(suma / sumg,6))
