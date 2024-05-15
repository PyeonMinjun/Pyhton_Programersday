n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
d = [[0] * 3 for _ in range(305)]

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1]+ arr[2])

else:
    d[1][1] = arr[1]
    d[1][2] = 0 
    d[2][1] = arr[2]
    d[2][2] = arr[1] + arr[2]

    for i in range(3,n+1):
        d[i][1] = max(d[i-2][1] , d[i-2][2]) + arr[i]
        d[i][2] = d[i-1][1] + arr[i]

    print(max(d[n][1],d[n][2]))

