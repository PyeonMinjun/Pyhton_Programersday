from collections import deque
t = int(input()) 

for _ in range(t):
    p = input()  # RDD
    n = int(input()) # 4
    ns = deque(input()[1:-1].split(","))
    
    if n == 0:
        ns = deque()
    print(ns)

    flag = 0
    rev = 0
    
    
    for i in p:
        if i == "R":
            rev += 1
        if i == "D":
            if ns:
                if rev % 2 == 0:
                    ns.popleft()
                else:
                    ns.pop()
            else:
                flag = 1
                print("error")
                break
                
            
    if flag == 0:
        if rev % 2 == 0:
            print("[{}]" .format(",".join(ns)))
        else:
            ns.reverse() 
            print("[{}]" .format(",".join(ns)))
            
        
  
    