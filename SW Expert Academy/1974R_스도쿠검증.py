def solve():
    for i in arr:
        if len(set(i)) != 9:
            return 0
    
    arr1 = list(zip(*arr))
    for j in arr1:
        if len(set(j)) != 9:
            return 0
    
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst =  arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    
    return 1

n = int(input())

for i in range(1,n+1):
    arr= [list(map(int,input().split())) for _ in range(9)]
    ans = solve()
    
    print("#{} {}" .format(i,ans))
    
    
    
    
   
    