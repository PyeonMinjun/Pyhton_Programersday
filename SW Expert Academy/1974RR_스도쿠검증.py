n = int(input())

for tc in range(1,n+1):
    res = 1
    ns = [list(map(int, input().split()))for _ in range(9)]
    
    for i in ns:
        if len(set(i)) != 9:
            res = 0
            
    arr1 = list(zip(*ns))
    for j in arr1:
        if len(set(j)) != 9:
            res = 0
            
    for k in range(0,9,3):
        for l in range(0,9,3):
            lst = ns[k][l:l+3] + ns[k+1][l:l+3] + ns[k+2][l:l+3]
            if len(set(lst)) != 9:
                res = 0
   
    print("#{} {}" .format(tc,res))