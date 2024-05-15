t= int(input())

s =  [0]+ [int(input()) for _ in range(t)]
d = [[0]*3 for _ in range(305)]

if t == 1:
    print(s[1])
    

else:
    d[1][1] = s[1]
    d[1][2] = 0
    d[2][1] = s[2]
    d[2][2] = s[1]+ s[2]

    for i in range(3,t+1):
        d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
        d[i][2] = d[i-1][1] + s[i]

    print(max(d[t][1], d[t][2]))