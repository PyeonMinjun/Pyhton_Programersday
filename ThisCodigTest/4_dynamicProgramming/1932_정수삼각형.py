n = int(input())
ns  = [0] + [ [0] + list(map(int,input().split())) for _ in range(n)]
d = [0] + [[0] * (n+1) for _ in range(n)]


d[1][1] = ns[1][1]

for i in range(2,n+1):
    d[i][1] = d[i-1][1] + ns[i][1]
    for j in range(2,i+1):
        if j == i:
            d[i][j] = d[i-1][j-1] + ns[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + ns[i][j]
    
        
print(max(d[n]))

