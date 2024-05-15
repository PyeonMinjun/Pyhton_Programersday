t = int(input())


for _ in range(t):
    n = int(input())
    d = [[0] * 2 for _ in range(n+1)]
    
    if n == 0:
        print(1, end= ' ')
        print(0)
    elif n == 1:
        print(0, end= ' ')
        print(1)
        
    else:
        d[0][0] = 1
        d[0][1] = 0
        d[1][0] = 0
        d[1][1] = 1
        
        for i in range(2,n+1):
            d[i][0] = d[i-1][0] + d[i-2][0]
            d[i][1] = d[i-1][1] + d[i-2][1]
        
        print(d[i][0],d[i][1])
    
    