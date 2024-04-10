t = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for tc in range(1,t+1):
    ns = []
    n, k = map(int,input().split())

    for i in range(n):
        mid,last,test = list(map(int,input().split()))
        ns.append((mid * 0.35) + (last * 0.45) + (test * 0.2))
        
    cnt = (n // 10) # 1
    target = ns[k-1]
    ns = list(reversed(sorted(ns)))
    finall_target = ns.index(target) // cnt
    
    print("#{} {}".format(tc, grades[finall_target]) )
    
    

