n= int(input())
ns = [0]+ [list(map(int,input().split())) for _ in range(n)]
d =  [0] + [[0]* 4 for _ in range(n)] 

d[1][1] = ns[1][0]
d[1][2] = ns[1][1]
d[1][3] = ns[1][2]


for i in range(2,n+1):
    d[i][1] = min(d[i-1][2], d[i-1][3]) + ns[i][0]
    d[i][2] = min(d[i-1][1], d[i-1][3]) + ns[i][1]
    d[i][3] = min(d[i-1][1], d[i-1][2]) + ns[i][2]

print(min(d[n][1], d[n][2],d[n][3]))
    
