n = int(input())

ns = [0] + [int(input()) for _ in range(n)] 
d = [[0] * 3 for _ in range(305) ]



if n == 1:
    print(ns[1])

else:
    
    d[1][1] = ns[1]
    d[1][2] = 0
    d[2][1] = ns[2]
    d[2][2] = ns[1] + ns[2]

    for i in range(3,n+1):
        d[i][1] = max(d[i-2][1], d[i-2][2]) + ns[i]
        d[i][2] = d[i-1][1] + ns[i]

    print(max(d[n][1], d[n][2]))