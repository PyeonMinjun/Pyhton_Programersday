def solve():
    for i in arr:
        if len(set(i)) != 9:
            return 0
    arr1 = list(zip(*arr))
    for j in arr1:
        if len(set(j)) != 9:
            return 0
        
    for k in range(0,9,3): # 0 3 6
        for l in range(0,9,3): # 0 3 6
            lst = arr[k][l:l+3] + arr[k+1][l:l+3] + arr[k+2][l:l+3]
            if len(set(lst)) != 9:
                return 0
            
    return 1
            

    
    

N = int(input())
for o in range(1,N+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = solve()
    print("#{} {}".format(o,ans))





   
        
        
            
        