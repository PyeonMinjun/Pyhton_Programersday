n = int(input())
d = [0] * 1005

d[1] = 1
d[2] = 2


if n == 1 or n == 2:
    print(n)
    exit(0)

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2] 
    
print(d[n]% 10007)