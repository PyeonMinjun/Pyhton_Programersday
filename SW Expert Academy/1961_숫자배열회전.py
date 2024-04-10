t = int(input())

for tc in range(1,t+1):
    arr = []
    
    n = int(input())
    
    
    for _ in range(n):
       arr.append(list(map(int, input().split())))
        
    arr90 = [[0] * n for _ in range(n)]
    arr180 = [[0] * n for _ in range(n)]
    arr270 = [[0] * n for _ in range(n)]
        
    for i in range(n):
        for j in range(n):
            arr90[i][j] = (arr[n-1-j][i])
            
    for i in range(n):
        for j in range(n):
            arr180[i][j] = (arr90[n-1-j][i])

            
    for i in range(n):
        for j in range(n):
            arr270[i][j] = (arr180[n-1-j][i])

    print("#{}" .format(tc))
             
    for a,b,c in zip(arr90,arr180,arr270):
        print("".join(map(str, a)), "".join(map(str, b)), "".join(map(str, c)))