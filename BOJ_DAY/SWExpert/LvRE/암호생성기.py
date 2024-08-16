for tc in range(1,11):
    t = int(input())
    ns = list(map(int,input().split()))
    flag = True
    while flag:
        for i in range(1,6):
            if ns[-1] <= 0:
                flag = False
                break
         
            ns[0] = ns[0] - i
            if ns[0] < 0:
                ns[0] = 0
                
            ns.append(ns.pop(0))
        
    print("#{} {}" .format(tc," ".join(map(str,ns))))
