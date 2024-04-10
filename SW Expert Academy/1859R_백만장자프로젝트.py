n = int(input())

for tc in range(1, n+1):
    n = int(input())
    ns = list(map(int,input().split()))
    ns = ns[::-1]
    sum = ns[0]
    res= 0
    
    for i in ns[1:]:
        
        if sum > i:
            res += sum - i
             
        else:
            sum = i
    
    print("#{} {}" .format(tc, res))
    