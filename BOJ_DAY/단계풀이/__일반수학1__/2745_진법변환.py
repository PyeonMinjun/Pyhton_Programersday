n, b = input().split()

n = "".join(reversed(n))

str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0 

for i in range(len(n)):
    nct = str.index(n[i])
    result += (nct * (int(b) ** i))
    
print(result)