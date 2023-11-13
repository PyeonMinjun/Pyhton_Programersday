t =int(input())
for tc in range(1,t+1):
    n = int(input())
    ns = list(map(int,input().split()))
    
    ns = ns[::-1]
    rm = ns[0]
    res = 0 
    for i in ns[1:]:
        if rm > i:
            res += rm - i
        else:
            rm = i
            
    print("#{} {}" .format(tc,res))